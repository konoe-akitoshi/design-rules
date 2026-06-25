# Philosophy

このフォルダーは、デザインルール全体の思想・判断軸をまとめる入口。
個別の理論や実装ルールに散らばっている「なぜそうするか」を、上位概念として参照できるようにする。

## 読む順序

1. [core-philosophy.md](./core-philosophy.md)
2. [design-philosophy-map.md](./design-philosophy-map.md)
3. 各思想の詳細ページ
4. [../principles/design-principles.md](../principles/design-principles.md)
5. [../theory/visual-design.md](../theory/visual-design.md)
6. [../theory/optical-adjustment.md](../theory/optical-adjustment.md)
7. [../../systems/border-radius.md](../../systems/border-radius.md)
8. [../../systems/responsive-mobile.md](../../systems/responsive-mobile.md)

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

## 思想ページ

各ページは、実装値や具体的なスタイル指定ではなく、思想の背景・中心概念・デザイン上の意味を整理するための参照ページ。
Wikipediaより少し実務寄り、Apple HIGより少し思想寄りの温度感で扱う。

### Systems Thinking

| Page | 内容 |
|------|------|
| [systems-thinking/README.md](./systems-thinking/README.md) | レイヤー索引 |
| [systems-thinking/systems-thinking.md](./systems-thinking/systems-thinking.md) | 最上位のシステム観 |
| [systems-thinking/cybernetics.md](./systems-thinking/cybernetics.md) | 観測、制御、フィードバック |
| [systems-thinking/buckminster-fuller.md](./systems-thinking/buckminster-fuller.md) | 全体システムを見る視点 |
| [systems-thinking/human-centered-systems-thinking.md](./systems-thinking/human-centered-systems-thinking.md) | 人間の認知と介入を含むシステム観 |
| [systems-thinking/pragmatism.md](./systems-thinking/pragmatism.md) | 実用性、検証、改善 |
| [systems-thinking/stewardship.md](./systems-thinking/stewardship.md) | 保守、長命性、変化への耐性 |

### Information Architecture

| Page | 内容 |
|------|------|
| [information-architecture/README.md](./information-architecture/README.md) | レイヤー索引 |
| [information-architecture/richard-saul-wurman.md](./information-architecture/richard-saul-wurman.md) | 情報設計と理解 |
| [information-architecture/legibility.md](./information-architecture/legibility.md) | 読める構造 |
| [information-architecture/massimo-vignelli.md](./information-architecture/massimo-vignelli.md) | 秩序、体系、一貫性 |
| [information-architecture/edward-tufte.md](./information-architecture/edward-tufte.md) | 情報密度、比較、誠実な可視化 |
| [information-architecture/christopher-alexander.md](./information-architecture/christopher-alexander.md) | パターン、再利用可能な構造 |

### Interaction Design

| Page | 内容 |
|------|------|
| [interaction-design/README.md](./interaction-design/README.md) | レイヤー索引 |
| [interaction-design/don-norman.md](./interaction-design/don-norman.md) | 認知、Affordance、Feedback |
| [interaction-design/jef-raskin.md](./interaction-design/jef-raskin.md) | 操作コスト、習熟、作業速度 |
| [interaction-design/calm-technology.md](./interaction-design/calm-technology.md) | 注意を奪いすぎない技術 |
| [interaction-design/ecological-psychology.md](./interaction-design/ecological-psychology.md) | 環境と関係性としての知覚 |
| [interaction-design/apple-hig.md](./interaction-design/apple-hig.md) | 明瞭さ、直接性、自然なフィードバック |

### Spatial Information

| Page | 内容 |
|------|------|
| [spatial-information/README.md](./spatial-information/README.md) | レイヤー索引 |
| [spatial-information/information-physicalization.md](./spatial-information/information-physicalization.md) | 情報の空間化、物理化、探索可能性 |

### Visual Design

| Page | 内容 |
|------|------|
| [visual-design/README.md](./visual-design/README.md) | レイヤー索引 |
| [visual-design/bauhaus.md](./visual-design/bauhaus.md) | 芸術と工学の統合 |
| [visual-design/dieter-rams.md](./visual-design/dieter-rams.md) | 抑制、誠実さ、長命性 |
| [visual-design/international-typographic-style.md](./visual-design/international-typographic-style.md) | グリッド、可読性、階層 |
| [visual-design/linear.md](./visual-design/linear.md) | 速度、静けさ、現代SaaSの作業感 |
