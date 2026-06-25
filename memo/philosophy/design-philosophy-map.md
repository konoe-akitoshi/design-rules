# Design Philosophy Map

UIデザイン単体ではなく、建築・工業デザイン・情報デザイン・メディアアートを含めた設計思想の地図。
このデザインシステムでは、最上位概念を **Systems Thinking** に置く。
哲学的な核は [core-philosophy.md](./core-philosophy.md) を参照。
詳細な理論・原則・実装ルールへ進む前の上位マップとして扱う。

## 目次

1. [中心思想](#中心思想)
2. [参照すべき思想](#参照すべき思想)
3. [設計判断への変換](#設計判断への変換)
4. [Akitoshi Design Stack](#akitoshi-design-stack)

---

## 中心思想

### Systems Thinking

このデザインシステムの主目的は、複雑なシステムを人間が理解・操作・制御できる形に翻訳すること。

デザインは目的ではなく、システムと人間の間にある翻訳層として扱う。

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

対象領域:

* サーバー
* ネットワーク
* Kubernetes
* CMS
* LLM
* ナレッジベース
* ロボット
* 可視化

共通する設計課題は、単に見た目を整えることではなく、情報・操作・状態変化・フィードバックの関係を扱える形にすること。

**基本方針**

* 個別のUI部品ではなく、システム全体の流れを先に見る
* 視覚表現は情報構造に従属させる
* 整理された構造が、そのまま理解しやすい構造だとは考えない
* 人間の認知・知覚・操作コストを通して構造を検証する
* 美しさは、システムが迷わず把握・操作できる状態から生まれるものとして扱う

---

## 参照すべき思想

### Cybernetics

観測、判断、制御、フィードバックを扱うシステム思想。

このデザインシステムでは、監視画面、Kubernetes Dashboard、Robot UI、AI Agentのような動的システムの基礎として扱う。

基本ループ:

```text
観測
↓
判断
↓
制御
↓
フィードバック
```

**UIへの適用**

* 画面は静的な情報置き場ではなく、状態を観測して介入するための制御面として設計する
* 異常、遅延、失敗、回復、次のアクションを同じ流れで読めるようにする
* ユーザーの操作結果を即座に返し、システムがどう変化したかを明確にする

### Buckminster Fuller

個別のモノではなく、システム全体を見るための参照点。

**UIへの適用**

* サーバー、ネットワーク、GPU、Kubernetes、LLMを個別部品ではなく相互依存するシステムとして扱う
* 画面単位ではなく、観測点、依存関係、ボトルネック、制御点の全体像を設計する
* Bauhausの「芸術と工学の統合」を、より大きなSystem Designの文脈に接続する

### Human-Centered Systems Thinking

システムを、インフラやデータだけでなく、人間の認知・判断・介入を含むものとして扱う思想。

**UIへの適用**

* ユーザーをシステムの外部観察者として扱わない
* 人間の判断と操作を含めてシステム全体を設計する
* 自動化できる部分と、人間が介入すべき部分を分ける
* 誤解、見落とし、操作ミスを設計対象に含める

### Pragmatism

思想や理論を、実際の作業改善に接続する立場。

**UIへの適用**

* 美学や理論より、実際の作業速度、理解、保守性を優先する
* 抽象的な好みではなく、再利用できる判断基準に落とす
* 一度で完成させるより、観測して改善できる形にする

### Stewardship

良いデザインを、作ることではなく、保守し続けることまで含めて考える思想。

**UIへの適用**

* 初期状態だけでなく、データ増加、障害、例外、権限変更に耐える構造にする
* 状態、履歴、責任範囲を追えるようにする
* 長期的に理解でき、修正できるUIを優先する

### Bauhaus

芸術と工学の統合。

**UIへの適用**

* 見た目、機能、実装都合を分離せず、同じ設計問題として扱う
* ロボット、Web、サーバー、可視化を横断する道具性を重視する
* 形は装飾からではなく、用途・素材・制約から導く

### Richard Saul Wurman

Information Architectureという概念を広めた人物のひとり。

思想:

> 情報は整理されて初めて理解できる。

**UIへの適用**

* 情報を表示する前に、分類軸、探索導線、検索性を設計する
* 初見で全体像を掴め、詳細へ自然に掘れる構造にする
* CMSや大学向けLLMでは、情報の所在と関係が分かることを最優先する

### Legibility

複雑なシステムを、人間が読める状態にするための思想。

Information Architectureの中核として扱う。

**UIへの適用**

* 現在地、全体像、詳細、依存関係、影響範囲が分かるようにする
* 異常と正常の差がすぐ読めるようにする
* 次に見るべき場所、次に取るべき行動が分かるようにする

### Massimo Vignelli

秩序を与えるデザインの基準。Vignelliは1972年のニューヨーク地下鉄図で知られる。

思想:

> デザインとは秩序を与えること。

**UIへの適用**

* CMS、ナレッジベース、ブログ、ネットワーク構成では分類体系を先に設計する
* 一覧、詳細、編集、検索、関連項目の導線を一貫させる
* 情報の例外をその場限りのUIで処理しない

### Edward Tufte

情報密度と明瞭さの基準。

思想:

> 装飾を減らし、情報密度を上げる。

**UIへの適用**

* ダッシュボード、監視画面、ネットワーク図では情報量を恐れない
* 空白は情報を薄めるためではなく、関係性を分けるために使う
* チャートや一覧では、装飾よりも比較・変化・異常検知を優先する

### Christopher Alexander

パターンによる設計の基準。A Pattern LanguageはソフトウェアのDesign Patternにも影響を与えた。

思想:

> 良い設計には再利用できるパターンがある。

**UIへの適用**

* 繰り返し現れる画面構造をコンポーネントとルールに落とす
* 例外的な見た目を増やさず、既存パターンを拡張する
* デザインルールは単発の好みではなく、再利用可能な判断基準として書く

### Don Norman

認知科学と人間中心設計の参照点。代表作は The Design of Everyday Things。

Information Architectureが構造を整理するなら、Normanはその構造が人間にどう認知されるかを問う。

重要な前提:

```text
整理された構造 ≠ 理解しやすい構造
```

**UIへの適用**

* 理論上正しい分類より、ユーザーが自然に発見・理解・操作できる構造を優先する
* Affordance、Signifier、Feedback、Mappingを明確にする
* 「設計者には分かる」ではなく「ユーザーがそう感じるか」を検証基準にする

配置:

```text
Information Architecture
        ↓
      Norman
        ↓
  UI / Interaction
```

### Jef Raskin

Macintoshプロジェクト初期に関わった人物。InterfaceではなくInteractionを設計する視点の参照点。

**UIへの適用**

* 画面の見た目より、操作コスト、認知負荷、作業速度を優先する
* Kubernetes Dashboard、CMS、Monitoring UI、Robot UIでは、ユーザーの作業フローを中心に設計する
* ショートカット、検索、連続操作、状態保持を作業速度のための設計要素として扱う

判断順:

```text
操作コスト
↓
認知負荷
↓
作業速度
```

### Calm Technology

目立たないテクノロジーの基準。

思想:

> テクノロジーは必要な時だけ注意を引く。

**UIへの適用**

* 通常状態では静かに、異常・未完了・要確認だけを明確にする
* 通知、アニメーション、色の強調を乱用しない
* 操作の主役はユーザーであり、UIは作業を邪魔しない

### Ecological Psychology

人が世界を記号ではなく、環境との関係性として知覚するという視点。

ネットワーク図、ノードグラフ、Kubernetesトポロジー、知識グラフと相性がよい。

**UIへの適用**

* ノードやカードを単独の記号としてではなく、距離、接続、向き、密度、クラスタの関係で読ませる
* 状態はラベルだけでなく、周辺要素との関係で理解できるようにする
* 情報空間を、ユーザーが探索できる環境として設計する

### Information Physicalization

情報を空間や物理的配置として扱う考え方。

関連するUI:

* Obsidian Graph
* GitHub Network
* 3D知識マップ
* トポロジー可視化
* 地図的UI
* ナレッジグラフ

**UIへの適用**

* 関係性のある情報は、リストだけでなく地図、ネットワーク、空間配置で表現する
* ノード、エッジ、距離、クラスタ、方向を意味のある視覚変数として扱う
* 3Dやグラフ表現は装飾ではなく、探索や理解に必要な場合に使う

### Dieter Rams

工業デザインにおける抑制と誠実さの基準。

特に重視する原則:

* Good design is unobtrusive
* Good design is honest
* Good design is as little design as possible

**UIへの適用**

* UIは主張しすぎず、作業対象を前に出す
* 機能を実際以上に見せる装飾を避ける
* 不要なカード、影、グラデーション、説明文を減らす

ただし、このシステムでは完全な静的ミニマルではなく、状態変化や操作感を伝えるための控えめな動きは許容する。

目安:

```
Rams 70%
Apple 30%
```

### International Typographic Style

スイスデザイン。階層、グリッド、可読性、情報の流れの基準。

**UIへの適用**

* グリッドで情報の読み順を作る
* 余白、サイズ、ウェイトで階層を明確にする
* 文字組みは装飾ではなく、構造化のために使う

### Linear

近年の開発者向けSaaSにおける高密度・高速・静かなUIの参照点。

特徴:

* 高速
* 自然なアニメーション
* 美しい余白
* 強い情報整理
* エンジニア向け

**UIへの適用**

* 操作レスポンスを軽くし、画面遷移や状態変化を短く自然にする
* 開発者向けUIでは、装飾よりも検索、ショートカット、一覧密度、状態把握を優先する
* Apple的な質感を持ちつつ、作業道具としての密度と速度を保つ

---

## 設計判断への変換

| 判断軸 | 採用する考え方 | UI上のルール |
|--------|----------------|-------------|
| 全体性 | Systems Thinking / Fuller | 画面単体ではなく、観測点、依存関係、制御点を含むシステム全体を見る |
| 制御 | Cybernetics | 観測、判断、制御、フィードバックのループをUI上で閉じる |
| 人間中心 | Human-Centered Systems Thinking | 人間の認知、判断、介入をシステムの一部として扱う |
| 実用性 | Pragmatism | 思想や理論を、実際の作業速度、理解、保守性に接続する |
| 保守性 | Stewardship | 初期状態だけでなく、変化・障害・保守に耐える構造にする |
| 読みやすさ | Legibility | 複雑なシステムを、現在地・関係・状態・次の行動が読める形にする |
| 情報量 | Tufte | 密度を下げすぎない。比較・異常・状態が同時に読めるようにする |
| 階層 | Swiss Style | グリッド、サイズ、ウェイト、余白で読み順を作る |
| 認知 | Don Norman | 理論上正しい構造ではなく、ユーザーが自然に理解できる構造にする |
| 操作 | Jef Raskin / Linear | 操作コスト、認知負荷、作業速度を優先する |
| 抑制 | Rams / Calm Technology | 装飾は減らし、必要な時だけ強調する |
| 秩序 | Vignelli / Wurman | 分類体系、導線、検索性を先に設計する |
| 再利用性 | Alexander | 画面ごとの特例を避け、パターンとして再利用する |
| 工学性 | Bauhaus | 見た目、機能、実装制約を一体で考える |
| 空間性 | Ecological Psychology / Information Physicalization | 関係性が重要な情報はグラフ、地図、トポロジーで表す |
| 操作感 | Linear / Apple | 高速で控えめなアニメーションを使い、作業を中断させない |

---

## Akitoshi Design Stack

中心:

```
Systems Thinking
    ↓
Information Architecture
    ↓
Interaction Design
    ↓
Visual Design
```

### Systems Thinking

* [Systems Thinking](./systems-thinking/systems-thinking.md): 最上位のシステム観
* [Cybernetics](./systems-thinking/cybernetics.md): 観測、判断、制御、フィードバック
* [Buckminster Fuller](./systems-thinking/buckminster-fuller.md): 個別部品ではなくシステム全体を見る
* [Human-Centered Systems Thinking](./systems-thinking/human-centered-systems-thinking.md): 人間の認知、判断、介入を含むシステム観
* [Pragmatism](./systems-thinking/pragmatism.md): 実際に使えること、試せること、改善できること
* [Stewardship](./systems-thinking/stewardship.md): 保守され、変化に耐える設計
* [Bauhaus](./visual-design/bauhaus.md): 芸術と工学の統合

### Information Architecture

* [Legibility](./information-architecture/legibility.md): 複雑なシステムを人間が読める形にする
* [Wurman](./information-architecture/richard-saul-wurman.md): 分類、探索、理解
* [Vignelli](./information-architecture/massimo-vignelli.md): 秩序、体系、一貫性
* [Tufte](./information-architecture/edward-tufte.md): 情報密度、比較、可視化
* [Alexander](./information-architecture/christopher-alexander.md): 再利用可能な設計パターン

### Interaction Design

* [Don Norman](./interaction-design/don-norman.md): 認知、Affordance、Feedback、Mapping
* [Jef Raskin](./interaction-design/jef-raskin.md): 操作コスト、認知負荷、作業速度
* [Calm Technology](./interaction-design/calm-technology.md): 静かなテクノロジー
* [Ecological Psychology](./interaction-design/ecological-psychology.md): 環境と関係性としての知覚
* [Apple HIG](./interaction-design/apple-hig.md): 直感性、質感、自然な動き

### Visual Design

* [Swiss Style](./visual-design/international-typographic-style.md): グリッド、可読性、階層
* [Dieter Rams](./visual-design/dieter-rams.md): 抑制、誠実さ、長命性
* [Linear](./visual-design/linear.md): 高速で開発者向けのSaaS体験
* [Information Physicalization](./spatial-information/information-physicalization.md): 情報の空間化、物理化、探索可能性

最終的な方向性:

> デザインは、複雑なシステムを人間が理解・操作・制御できる形に翻訳するための手段である。
