# LeoSoft Industrial SDKs for .NET

[![SDK tests](https://github.com/leosoft-tw/leosoft-sdk-quality/actions/workflows/sdk-tests.yml/badge.svg)](https://github.com/leosoft-tw/leosoft-sdk-quality/actions/workflows/sdk-tests.yml)

LeoSoft builds ready-to-integrate .NET SDKs for semiconductor and factory equipment makers.
Every release is built and tested automatically on Windows and Linux, .NET 8 and .NET 10.

## GEM200 SDK — SECS/GEM for equipment

**Problem:** your machine must talk to the factory host over SECS/GEM (HSMS) before it can ship, and writing that layer from scratch takes months.
**For:** equipment makers and automation engineers adding SECS/GEM to new or existing machines.
**Track record:** field-tested with factory hosts at multiple semiconductor packaging & test facilities.

## GEM300 SDK — 300 mm automation

**Problem:** 300 mm fabs require the GEM300 standards on top of basic GEM.
**For:** equipment makers selling into 300 mm production lines. Includes everything in GEM200.

## AI-AOI SDK — vision inspection

**Problem:** manual or rule-only visual inspection is slow and hard to keep consistent.
**For:** machine builders and integrators who need shape matching and defect detection inside their own C# / VB.NET software. Every NG result reports the reason, measured value, threshold and location.
**Track record:** OpenCV-based inspection at 40,000 UPH, with a pass/fail decision in under 90 ms per unit (actual throughput depends on the line, optics and part).

## Tested on

| | Windows | Linux |
|---|---|---|
| .NET 8 | ✅ | ✅ |
| .NET 10 | ✅ | ✅ |

The badge above shows the latest automated run. SDK source code is private; this repository only shows pass/fail results.

## Quotes & 30-day trial

- Email: [leosoft.tw@gmail.com](mailto:leosoft.tw@gmail.com)
- LINE: [@076cbubi](https://line.me/R/ti/p/@076cbubi)
- Website: [leosoft-hub.pages.dev](https://leosoft-hub.pages.dev) · [SECS/GEM](https://leosoft-secs-gem.pages.dev) · [AI-AOI](https://leosoft-ai-aoi.pages.dev)

## 繁體中文摘要

LeoSoft 提供 .NET 工業 SDK：GEM200、GEM300（SECS/GEM 設備通訊）與 AI-AOI（影像檢測）。GEM200 已在多家半導體封測廠實測；AI-AOI 檢測達 40,000 UPH、每顆 90 ms 內判定（實際產能依產線、光學與料件而定）。每次發行都在 Windows／Linux、.NET 8／.NET 10 自動測試，本倉庫只公開測試結果，不含原始碼。詢價與 30 天試用：leosoft.tw@gmail.com、LINE @076cbubi。
