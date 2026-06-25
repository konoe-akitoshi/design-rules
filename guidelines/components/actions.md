# アクション — コンポーネント詳細

ユーザーが操作を起こす・別リソースへ移る部品。[共通規則](./README.md#どのコンポーネントも継承する共通規則universal)（signifier・focus・hover/active/disabled・ヘアライン・コントラスト）は各仕様で繰り返さない。値は [`tokens.json`](../../tokens.json) / [`values/color-system.md`](../values/color-system.md)。

---

### Button  〔—〕

**用途** … アクションを起動する（保存・送信・削除など、状態を変える/処理を走らせる）。**移動・遷移は Link**、操作は Button。
**変種** … primary（主要操作・面）/ secondary（線）/ ghost（地なし・低優先）/ danger（破壊操作）。**1画面の primary は1つ**に絞る（[03](../03-interaction-feedback.md) Calm 注意の階層）。
**構成** … 動詞ラベル＋任意で先頭アイコン。アイコン単独は → Icon。
**寸法** … padding `12px 20px`（`py-3 px-5`・1:1.67）/ radius `6px`（`rounded-md`・golden L2）/ 高さ・当たり判定 最小 `48px`（[10](../10-accessibility.md)）/ ラベルは `translateY(-1px)` で cap-height 上方補正。
**色** … primary=地 `--c-accent`＋文字 `--c-on-accent`、hover/active `--c-accent-ink`。secondary=地 `--c-surface`＋線 `--c-line-strong`＋文字 `--c-ink`。ghost=地なし＋文字 `--c-accent`、hover 地 `--c-sunk`。danger=地 `--c-danger`＋文字 `--c-on-accent`（淡形は地 `--c-danger-bg`＋文字 `--c-danger`）。disabled=文字 `--c-quiet`＋地 `--c-sunk`（彩度を上げない）。
**状態** … default / hover（accent→accent-ink・面→sunk）/ active（押下）/ focus / disabled（`cursor:not-allowed`）/ loading（spinner＋ラベル維持、二度押し防止で不活性、押下は即 FB）。
**規則** … 03 Norman/Apple — 押下に即時 FB、送信中は loading を返す。**破壊操作は undo 優先**、確認モーダルは不可逆な操作だけ（`M-RECOVERABILITY`）。コピーは動詞（「保存」「削除」）、曖昧アイコンにはラベル併用（Apple Clarity）、**フロー全体で同じ語**を使う（「保存」と「適用」を混在させない）。
**a11y** … ネイティブ `<button type>`（遷移は `<a>`）。Enter/Space で実行。アイコンのみは `aria-label` 必須。loading 中は `aria-busy="true"`。
**関連** … Button group / Link / Dropdown menu / Icon。

---

### Button group  〔Toolbar〕

**用途** … 関連するボタンを隣接させ、1つの操作単位として見せる（整列・書式・ページ操作など）。
**変種** … 連結（境界を共有）/ 分離（`gap 8px`）/ split button（主操作＋付随メニュー）。
**構成** … 2つ以上の Button。意味のかたまりは Separator で割る。
**寸法** … 連結時は内側 radius 0・両端のみ角丸で境界線共有、分離時は `gap 8px`。各ボタンで最小 `48px`・間隔 `8px` を維持（[10](../10-accessibility.md)）。
**色** … 群は secondary 系（地 `--c-surface`＋線 `--c-line-strong`）で統一し、**主操作だけ primary**。連結時の仕切りは `--c-line`。
**状態** … 各ボタンが個別に hover/active/focus/disabled。トグル群なら選択中を地 `--c-accent-sunk`＋文字 `--c-accent` で明示（→ Segmented control）。
**規則** … 03 — 近接で「1単位」と分かるよう **群内余白 < 群間余白**。[07](../07-restraint-form.md) Rams — 区切りは影でなくヘアライン。注意を集中させるため primary は群内で1つ。
**a11y** … `role="toolbar"`、左右矢印でボタン間移動（Tab は群を1ストップに）。各ボタンはネイティブ `<button>`。
**関連** … Button / Segmented control / Dropdown menu。

---

### Link  〔Anchor〕

**用途** … 別ページ・別リソース・ページ内位置へ**移動**する。**遷移は Link・操作は Button**（この使い分けが核）。
**変種** … インライン（本文内）/ スタンドアロン / ナビの現在地リンク。外部・新規タブ・ファイル DL は明示。
**構成** … 文脈で目的が分かるテキスト（「こちら」を避ける）＋任意で外部/DL アイコン。
**寸法** … 本文行内は padding 不要・下線で判別。ナビ等の独立リンクは当たり判定 `48px` を確保。
**色** … 文字 `--c-accent`＋**下線**、hover `--c-accent-ink`。色だけで判別させず下線を併用（10 色非依存）。
**状態** … default（下線）/ hover（accent-ink）/ focus / visited（任意）/ active。
**規則** … 03 Apple — 「戻る」「遷移」を期待通りに動かす。10 — リンクを色のみで示さず下線・記号を併用。外部リンク・新規タブ・DL は結果を予告する（Norman: 操作前に結果を伝える）。
**a11y** … 遷移は必ず `<a href>`（`<div onclick>` 不可）。**Enter で実行（Space は不可＝Button との差）**。新規タブは `rel="noopener"`＋visually-hidden で「新規タブで開く」を補う。アイコンのみは `aria-label`。
**関連** … Button（操作との使い分け）/ Breadcrumbs / Navigation。

---

### Dropdown menu  〔Select menu〕

**用途** … ボタンから、操作（コピー・削除）や遷移（移動）の**メニュー**を開く。値を選ぶフォーム入力は Select（こちらは入力ではない）。
**変種** … アクションメニュー / コンテキストメニュー（右クリック）/ split button の付随メニュー。
**構成** … トリガー（Button＋`▾`）＋ポップアップのリスト（項目・Separator・破壊項目は末尾に danger 色で隔離）。
**寸法** … 面 radius `10px`（golden L1）/ 項目 padding `8px 16px` 系・高さ最小 `44px` / トリガーの `▾` は重心を錯視補正で合わせる。
**色** … 面 `--c-surface`＋境界 `--c-line`（影でなくヘアライン）/ 項目 hover 地 `--c-sunk` / 選択中 `--c-accent-sunk`＋`--c-accent` / 破壊項目 `--c-danger`。
**状態** … 閉/開（`aria-expanded`）/ 項目 hover・active・focus・disabled / 破壊項目は danger。開閉に即時 FB。
**規則** … 03 Raskin — 頻出操作のクリック数を減らす。Apple Clarity — 各項目は動詞ラベル、曖昧アイコンにラベル。07 — 装飾でなくヘアラインで面を分ける。破壊項目は undo 前提、確認は不可逆時のみ。
**a11y** … トリガーは `<button aria-haspopup="menu" aria-expanded>`、メニューは `role="menu"` / 項目 `role="menuitem"`。↑↓ で移動、Enter/Space で実行、Esc で閉じてトリガーへ focus 復帰。
**関連** … Button / Select（forms）/ Popover / Segmented control。

---

### Segmented control  〔Toggle button group〕

**用途** … 排他的な選択肢・ビューを切替える（リスト/グリッド、日/週/月）。切替は即時反映し、**現在選択を常時明示**。
**変種** … 2〜5項目の単一選択（多数は Select / Tabs へ）。アイコン＋ラベル / テキストのみ。
**構成** … 連結したトグルボタンの帯。常に1つだけが選択状態。
**寸法** … 帯 radius `6px`、内側セグメントは角丸を共有（両端のみ丸）。各セグメント 最小 `44–48px`・padding `12px 20px` 系。
**色** … トラック地 `--c-sunk`、選択中=`--c-surface` 面＋`--c-accent` 文字（または地 `--c-accent-sunk`＋`--c-accent`）、非選択=`--c-muted` 文字、仕切り `--c-line`。
**状態** … 選択/非選択 / hover（非選択を濃く）/ focus / disabled。選択は**色＋面**の二重符号（色だけにしない）。
**規則** … 03 Norman — 現在選択がひと目で分かる mapping。Calm — 平常は静かに、選択だけ前景化。10 — 選択を色のみで伝えない（面・太字も併用）。切替は即 FB（ビューが即変わる）。
**a11y** … 単一選択なら `role="radiogroup"`＋各 `role="radio" aria-checked`、左右矢印で移動。複数パネルを切替えるなら Tabs（`role="tablist"`）を検討。
**関連** … Tabs / Toggle（forms）/ Button group / Radio button。

---

### Icon  〔アイコンボタン〕

**用途** … 目的・対象を示す図記号。装飾でなく**意味を運ぶ**ときだけ置く。操作を兼ねるものがアイコンボタン。
**変種** … 意味アイコン（テキスト併走）/ アイコンボタン（単独操作）/ トグルアイコン（★/☆ 等、状態を持つ）。
**構成** … SVG（絵文字でなく SVG・[07](../07-restraint-form.md) Linear）。アイコンボタンは 視覚 `24px`＋padding `12px`＝当たり判定 `48px`。
**寸法** … 視覚 `24px`＋padding `12px`＝`48px`（[10](../10-accessibility.md) Fitts）。背景 radius `4px`（golden L3）。`▶` 等の三角は尖端方向へ H/6 オフセット、円形は 3〜5% オーバーシュート（錯視補正）。
**色** … `--c-muted`（標準）/ `--c-ink`（強調）/ `--c-accent`（操作・現在）。hover 地 `--c-sunk`。状態は色だけで伝えない。
**状態** … default / hover（地 sunk）/ active / focus / disabled（`--c-quiet`）/ トグルは on/off。
**規則** … 03 Apple Clarity — **曖昧なアイコン単独は意味が伝わらない**。可視ラベルか tooltip＋`aria-label` を必ず添える。07 — 意味を運ばないアイコンは削る（削減テスト）。
**a11y** … 操作するなら `<button aria-label>`。単独アイコンは `aria-label` 必須、装飾アイコンは `aria-hidden="true"`。トグルは `aria-pressed`。Enter/Space で実行。
**関連** … Button / Tooltip / Dropdown menu / Badge。

---

### Skip link  〔Screenreader skip〕

**用途** … キーボード/支援技術ユーザーが、繰り返すヘッダ・ナビを飛ばして**本文（main）へ直接移動**する。
**変種** … 「本文へスキップ」単独 / 複数リンク（本文・主ナビ・検索へ）。
**構成** … ページ最初のフォーカス可能要素 `<a href="#main">`。普段は隠れ、**focus で初めて可視**。
**寸法** … focus 時に左上へ出現、padding `8px 16px`、radius `6px`、当たり判定 `48px`、重なり最前面。
**色** … 地 `--c-accent`＋文字 `--c-on-accent`（or 地 `--c-surface`＋線 `--c-line-strong`）。focus リングを必ず可視。
**状態** … 非 focus（視覚的に隠すが DOM には存在）/ focus（画面内に出現）/ activate（`#main` へ移動し focus を移す）。
**規則** … [10](../10-accessibility.md) — キーボードだけで操作完結・focus 可視。`display:none` で消すと**フォーカス不能**になるためオフスクリーン手法で隠す。Norman/Apple — 移動先を明示（「本文へスキップ」）。
**a11y** … ページ先頭・Tab 最初の要素。遷移先 `<main id="main" tabindex="-1">`。Enter で移動。visually-hidden は clip 手法（読み上げには残す）。
**関連** … Visually hidden / Navigation / Header / Link。
