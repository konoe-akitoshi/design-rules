# Philosophy

このフォルダーは、デザインルール全体の思想・判断軸をまとめる入口。
個別の理論や実装ルールに散らばっている「なぜそうするか」を、上位概念として参照できるようにする。

## 読む順序

1. [core-philosophy.md](./core-philosophy.md)
2. [design-philosophy-map.md](./design-philosophy-map.md)
3. [../principles/design-principles.md](../principles/design-principles.md)
4. [../theory/visual-design.md](../theory/visual-design.md)
5. [../theory/optical-adjustment.md](../theory/optical-adjustment.md)
6. [../systems/border-radius.md](../systems/border-radius.md)
7. [../systems/responsive-mobile.md](../systems/responsive-mobile.md)

## 役割分担

| 場所 | 役割 |
|------|------|
| `philosophy/` | 哲学的な核と思想地図。Systems Thinking、Information Architecture、Interaction Designなど |
| `principles/` | 実用原則。Dieter Rams 10原則、UI/UX Lawsなど |
| `theory/` | 理論的根拠。ゲシュタルト、色彩、錯視、認知など |
| `systems/` | 実装ルール。spacing、radius、responsiveなど |

## 中心軸

このデザインシステムの最上位概念は **Systems Thinking**。

デザインは目的ではなく、複雑なシステムを人間が理解・操作・制御できる形に翻訳するための手段として扱う。

基本レイヤー:

```text
Systems Thinking
    ↓
Information Architecture
    ↓
Interaction Design
    ↓
Visual Design
```

基本方針:

* 個別の画面よりシステム全体
* 装飾より情報構造
* 雰囲気より分類・階層・関係性
* 見た目の派手さより状態把握と操作速度
* 静的な表示より観測・判断・制御・フィードバック
* 理論上の正しさより人間の認知・知覚上の自然さ
* 作って終わりではなく、保守され変化に耐えること
