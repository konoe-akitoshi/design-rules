# Stewardship

## 概要

Stewardshipは、設計を「作って終わり」ではなく、長く扱い、保守し、変化に耐えさせる責任として捉える考え方。
一時的な完成度よりも、運用、継続性、修正可能性、引き継ぎ可能性を重視する。

このデザインシステムでは、Stewardshipを長命性と保守性の思想として扱う。

## 背景

Stewardshipは、資源管理、環境、組織運営、ソフトウェア保守、プロダクト運用などで重要になる考え方。
デザインの領域では、短期的な印象やローンチ時の完成度だけでなく、長期的に使われる構造が問われる。

特に、CMS、ナレッジベース、管理画面、運用ツール、AIシステムでは、データや利用者、権限、例外が増えていく。
その変化に耐えないUIは、時間とともに読めなくなる。

## 中心的な考え方

* 良い設計は長く保守できる
* 変化を想定する
* 例外状態を隠さない
* 引き継ぎ可能な構造にする
* 履歴と責任範囲を扱えるようにする

## 代表的な概念

### Maintenance

設計されたものを継続的に修正し、保つ行為。
UIでは、データ追加、仕様変更、権限変更、コンポーネント拡張が関係する。

### Longevity

長く使えること。
Dieter Ramsの「Good design is long-lasting」と接続する。

### Accountability

誰が、いつ、なぜ変更したかを追えること。
特に管理画面や運用UIで重要になる。

### Graceful Degradation

理想状態でなくても、意味を保ちながら使い続けられること。

## デザインにおける意味

Stewardshipは、UIを一枚の完成絵としてではなく、時間の中で変化する仕組みとして見る。
良いUIは、初期データが少ない時だけ美しいのではなく、情報が増え、例外が発生し、利用者が変わっても読める。

## このデザインシステムとの関係

このデザインシステムでは、StewardshipをRamsの長命性、Systems Thinkingの全体性、Pragmatismの実用性と接続する。
見た目の洗練は重要だが、保守できない洗練は弱い設計とみなす。

## 関連する思想

* Dieter Rams
* Pragmatism
* Systems Thinking
* Christopher Alexander

## 参考

* Long-lived design
* Software maintenance
* Design systems governance
* Sustainable design

