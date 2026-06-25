---
name: baseline-ui
description: 生成済みのUIコードを、スペーシング・タイポグラフィ・錯視補正の観点でガイドラインに沿ってポリッシュする。4pt/8ptグリッド、非対称パディング、黄金比角丸、タイプ階層、錯視補正(重心オフセット/オーバーシュート/cap-height)を適用する。UI生成後の仕上げ段で使用。
argument-hint: "[ファイルパス or コードスニペット]"
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Baseline UI — スペーシング・タイポ・錯視のポリッシュ

生成済み UI の「土台の精度」を ガイドライン に沿って整える。新規生成ではなく**既存コードの修正**。

## 読み込む

1. `${CLAUDE_SKILL_DIR}/../../../guidelines/04-layout-space.md` — グリッド・非対称padding・近接・錯視補正
2. `${CLAUDE_SKILL_DIR}/../../../guidelines/06-typography.md` — タイプ階層・スケール・読み順
3. `${CLAUDE_SKILL_DIR}/../../../tokens.json` — spacing / asymmetricPadding / opticalSpacing / opticalAdjustment（値の正）

錯視補正の根拠は 04-layout-space.md に内包。

## 対象

$ARGUMENTS

## 適用する調整

### スペーシング（04 / tokens.json）
- 4の倍数以外の値を 4/8/12/16/24/32 等へ寄せる
- 縦横同値の padding を非対称へ（カード `16px 24px`、ボタン `12px 20px`、タグ `4px 12px`、フォーム `8px 16px`）
- Visual Rhythm: 見出し下は広め、段落間は控えめ、セクション間は明確に（機械的な等間隔を崩す）
- 近接: 関連要素を近づけ、無関係を離す

### タイポグラフィ（06）
- サイズ・ウェイトの差を重要度の差に一致させる（装飾目的のサイズ変更を削る）
- 限定したタイプスケールへ寄せる（中間値を作らない）
- 行長・行間を本文の可読範囲に整える

### 錯視補正（04 / optical-adjustment）
- 三角形アイコンを尖端方向へ H/6（≈16.7%）オフセット
- 円形アイコンを 3〜5% 拡大（オーバーシュート）
- ボタンテキストを `translateY(-1px)` で上方向補正
- 太字下余白 ×0.75 / 軽いテキスト下余白 ×1.25

## 進め方

1. 対象を読み、上記カテゴリの逸脱を洗い出す
2. tokens.json の値に厳密に合わせて Edit する（推測値を入れない）
3. 変更点を「箇所 / 現在 → 修正 / 根拠(ガイドライン章)」で要約して報告する

構造・配色・装飾の是非には踏み込まない（それぞれ composition-patterns / 05 color / 07 restraint-form の領分）。土台の精度だけを上げる。
