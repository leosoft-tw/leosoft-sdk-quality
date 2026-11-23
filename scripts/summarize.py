import argparse
import contextlib
import io
import os
from pathlib import Path
import tempfile
import xml.etree.ElementTree as ET


def summarize(results_dir, runner_os, tfm):
    prefix = f"RESULT os={runner_os} tfm={tfm}"
    totals = dict.fromkeys(("total", "passed", "failed", "notExecuted"), 0)
    found = False
    try:
        for report in results_dir.rglob("*.trx"):
            counters = ET.parse(report).findall("./{*}ResultSummary/{*}Counters")
            if not counters:
                raise ValueError
            for counter in counters:
                for key in totals:
                    count = int(counter.attrib[key])
                    if count < 0:
                        raise ValueError
                    totals[key] += count
            found = True
    except (ET.ParseError, KeyError, OSError, ValueError):
        found = False

    if not found:
        print(f"{prefix} build=failed")
        return 1

    print(
        f"{prefix} total={totals['total']} passed={totals['passed']} "
        f"failed={totals['failed']} skipped={totals['notExecuted']}"
    )
    return int(totals["failed"] > 0)


def self_test():
    sample = """<TestRun xmlns="http://microsoft.com/schemas/VisualStudio/TeamTest/2010">
      <ResultSummary>
        <Counters total="4" passed="2" failed="1" notExecuted="1" />
      </ResultSummary>
    </TestRun>"""
    with tempfile.TemporaryDirectory() as tmp:
        results_dir = Path(tmp)
        nested = results_dir / "nested"
        nested.mkdir()
        (results_dir / "first.trx").write_text(sample, encoding="utf-8")
        (nested / "second.trx").write_text(sample, encoding="utf-8")
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            status = summarize(results_dir, "Linux", "net8.0")
        assert status == 1
        assert output.getvalue() == (
            "RESULT os=Linux tfm=net8.0 total=8 passed=4 failed=2 skipped=2\n"
        )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("results_dir", type=Path, nargs="?")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    if args.results_dir is None:
        parser.error("a results directory is required")
    return summarize(
        args.results_dir, os.environ.get("RUNNER_OS", "unknown"), os.environ.get("TFM", "unknown")
    )


if __name__ == "__main__":
    raise SystemExit(main())
