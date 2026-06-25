# Systems Thinking

## 概要

Systems Thinkingは、対象を孤立した部品ではなく、相互作用する要素の集合として見る考え方。
原因と結果を直線的に扱うのではなく、関係、循環、遅延、制約、フィードバックを含む全体として捉える。

このデザインシステムでは、Systems Thinkingを最上位の思想として扱う。
UIは画面単体ではなく、情報、操作、ユーザー、運用、変化を含むシステムの一部である。

## 背景

Systems Thinkingは、工学、組織論、生態学、制御理論、経営、社会システム論などで発展してきた。
複雑な問題では、個別要素を最適化しても全体の振る舞いが良くなるとは限らない。
むしろ、要素間の関係やフィードバック構造を理解することが重要になる。

UIデザインでも同じことが起きる。
個別のボタン、カード、画面が整っていても、ユーザーが全体の流れを理解できなければ良い設計にはならない。

## 中心的な考え方

* システムは要素ではなく関係で成り立つ
* 問題は単一の原因ではなく、構造から生まれる
* 変化には遅延と副作用がある
* フィードバックはシステムの振る舞いを決める
* 部分最適は全体最適と一致しない

## 代表的な概念

### Feedback

出力が入力に戻り、次の振る舞いに影響する構造。
UIでは、操作結果、状態変化、通知、ログ、確認がこれにあたる。

### Boundary

どこまでを同じシステムとして見るかという境界。
UIでは、ユーザー、データ、権限、運用、保守者まで含めるかが問題になる。

### Leverage Point

小さな介入で大きな変化が起きる箇所。
設計では、画面全体を作り替えるより、分類軸やフィードバックの場所を変える方が効くことがある。

### Emergence

個別要素からは予測しにくい全体の振る舞い。
複雑なプロダクトでは、機能追加によって認知負荷や操作ミスが増えることがある。

## デザインにおける意味

Systems Thinkingは、UIを単なる表示面ではなく、システムと人間の接点として扱う。
良いUIは情報を並べるだけでなく、ユーザーが全体の状態、制約、変化の方向を理解できるようにする。

この視点では、画面は以下を担う。

* 状態を観測する
* 関係を読む
* 判断を支援する
* 介入点を示す
* 結果をフィードバックする
* 次の保守や改善につなげる

## このデザインシステムとの関係

このデザインシステムでは、Systems Thinkingを最上位に置く。
Information Architecture、Interaction Design、Visual Designは、すべてSystems Thinkingの下位レイヤーとして扱う。

```text
Systems Thinking
    ↓
Information Architecture
    ↓
Interaction Design
    ↓
Visual Design
```

つまり、見た目を決める前に、対象がどのようなシステムで、ユーザーがどこで理解し、どこで判断し、どこで介入するかを考える。

## 関連する思想

* Cybernetics
* Buckminster Fuller
* Human-Centered Systems Thinking
* Stewardship
* Information Architecture

## 参考

* General Systems Theory
* Cybernetics
* Donella Meadows, Thinking in Systems
* Peter Senge, The Fifth Discipline

