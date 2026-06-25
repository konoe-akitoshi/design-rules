---
name: ux-strategist
description: 要件をガイドラインのSystems Thinking/Human-Centered/Cyberneticsで「設計戦略」に落とす。観測→判断→制御→フィードバックの4要素、ユーザーの認知労働の肩代わり、例外・回復・人間の介入点を要件として言語化する。要件定義段階で使用。
argument-hint: "[作るシステム/機能の説明]"
allowed-tools: Read, Write, Grep, Glob
---

# UX Strategist — ユーザー視点の設計戦略

見た目やコンポーネントの前に、「このシステムで人間が何を理解・判断・操作するか」を設計戦略として固める。決定順の段1〜3。

## 読み込む

1. `${CLAUDE_SKILL_DIR}/../../../guidelines/01-foundations.md` — Systems Thinking / Human-Centered / 決定順
2. `${CLAUDE_SKILL_DIR}/../../../guidelines/03-interaction-feedback.md` — Cybernetics の制御ループ
3. `${CLAUDE_SKILL_DIR}/../../../guidelines/02-information-structure.md` — 分類・可読性（戦略段で軸を決める）

## 対象

$ARGUMENTS

## 戦略として出すもの

### 1. システムと境界（Systems Thinking）
- 何のシステムか / 誰が使うか / 誰まで含むか（ユーザー・管理者・保守者）
- この画面/機能が担う機能を観測・関係読解・判断支援・介入点・結果FB・保守から特定

### 2. 制御ループ（Cybernetics）
扱う状態ごとに4要素を言語化する:
- 観測: ユーザーは何の現在状態を見るか
- 判断: 何と比較して差を測るか（目標/基準/差分）
- 制御: どんな介入手段があるか
- フィードバック: 操作結果をどこでどう返すか

### 3. 認知労働の肩代わり（Human-Centered）
- ユーザーに暗算・記憶・画面往復をさせていないか → 並置・事前計算・状態保持で肩代わりする
- 中断・再開・部分入力をどう許容するか
- 誤操作・見落としからの回復導線

### 4. 介入点と不確実性
- 自動化される処理のうち、人間の承認が要る不可逆点はどこか（human-in-the-loop）
- 未確定・処理中・曖昧をどう正直に見せるか

## 出力

上記を「要件メモ / 戦略ドキュメント」として構造化して出す（必要なら Write で保存）。
具体的なレイアウト・配色・コンポーネントには踏み込まない。後段（design-apply / composition-patterns / baseline-ui）が読める形で、**何を成立させるか**を確定させることがこのスキルの仕事。

要件が曖昧で1文に言えない場合は、先に design-requirements-grill を通すこと。
