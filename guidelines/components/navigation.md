# ナビゲーション — コンポーネント詳細

リンクの容器と移動装置。共通の核は「**現在地が読めること**」と「**入口と出口を欠かさず行き止まりを作らないこと**」。値は [`../../tokens.json`](../../tokens.json) / [color-system](../values/color-system.md)、共通規則は [README](./README.md#どのコンポーネントも継承する共通規則universal) を継承する。

---

### Navigation 〔Nav / Menu〕

**用途** … サイト/アプリの主要リンクをまとめ、押せる選択肢と現在地を提示する容器。Header・Footer・サイドバー・bottom-nav が中身として再利用する基底部品。
**変種** … 水平（ヘッダー）/ 垂直（サイドバー）/ 下部固定（モバイル bottom-nav）/ オーバーフロー（「もっと見る」格納）。
**構成** … `nav` > `ul` > `li` > `a`。任意でアイコン・グループ見出し・現在地マーカー（左/下の `--c-accent` バー）。
**寸法** … 各リンクのタッチ高さ最小 44–48px（`touchTargets`）、項目間 `gap:8px`（spacing-2）。リンク padding `8px 16px`（formField 1:2）、hover/active 地の radius `6px`（golden-2）。
**色** … 通常リンク `--c-muted`、hover で文字 `--c-ink` ＋地 `--c-sunk`。現在地（active）は文字 `--c-accent` ＋地 `--c-accent-sunk`。
**状態** … default（muted）/ hover（ink＋sunk）/ active＝現在地（accent＋accent-sunk＋マーカー）/ focus（共通 outline）/ disabled（quiet・操作不可）。
**規則** … 02 Legibility：現在地は必ず読める＝active を色だけでなくマーカーやウェイトでも明示（Landmark）。Wurman：一覧・詳細・関連への入口を網羅し、どの画面からも出口がある（行き止まり禁止）。モバイルは主導線を下部に置き親指ゾーン＋`safe-area-inset` を適用。
**a11y** … `<nav aria-label="主ナビ">`（同一ページに複数 nav があれば各々ラベル）。現在地リンクに `aria-current="page"`。`ul`/`li` で構造化、Tab で移動・Enter で遷移。
**関連** … Header / Footer / Breadcrumbs / Tabs / Tree view / Drawer。

---

### Header

**用途** … 全ページ上部の帯。サイト名（ホームへの出口）＋主ナビ＋主要アクション（検索・アカウント）を一定位置に固定し、現在地と移動手段を常時供給する。
**変種** … 静的 / `sticky`（スクロール追従）/ 透過→不透過に変化 / モバイルはハンバーガーで Drawer 展開。
**構成** … `header` 内に ロゴ（左）｜主 Navigation（中央/左）｜ユーティリティ（右）。下辺はヘアライン `--c-line` で分離（影でなく境界）。
**寸法** … 高さ 56–64px、左右 padding `16–24px`（spacing-4/6）。各操作のタッチ最小 44–48px、間隔 8px。sticky 時は下辺 `--c-line` のみで段差を示す。
**色** … 地 `--c-surface`、文字 `--c-ink`／ナビ項目は Navigation の規約（muted→ink、現在地 accent）。背景に影・グラデーションを敷かない。
**状態** … リンク/ボタンは Navigation と同一。sticky の影は付けず境界線で前後関係を示す（装飾的 depth 禁止）。
**規則** … 02 Legibility：全画面で同じ位置に出し、ロゴ＝常設の出口、現在地を active で示す。Wurman：ここが主要ナビの「入口」、検索も併設し迷子の回収口を作る。モバイルはハンバーガーを上部・主 CTA は下部へ分離。
**a11y** … `<header>` ＋ 中の `<nav aria-label="グローバル">`。ロゴリンクは可視テキストか `aria-label="ホーム"`。ハンバーガーは `button aria-expanded` ＋ `aria-controls`、Esc で閉じる。
**関連** … Navigation / Drawer / Search input / Breadcrumbs / Footer。

---

### Footer

**用途** … ページ下部。著作権・法務（規約/プライバシー）・サイトマップ的な関連リンクを集約し、本文を読み切った人へ次の出口を提供する。
**変種** … 単段（小規模）/ 多カラム（リンク群＋ニュースレター）/ アプリ簡易（コピーライトのみ）。
**構成** … `footer` 内に リンク群（カラム見出し＋ `ul`）｜法務行｜任意でロゴ・SNS。上辺ヘアライン `--c-line` で本文と分離。
**寸法** … 上下 padding `32–48px`（spacing-8/12）、カラム間 `gap:24–32px`。リンク行高さ 44px 以上、密集時も間隔 8px。
**色** … 地 `--c-canvas` か `--c-surface`、見出し `--c-ink-soft`、リンク `--c-muted`→hover `--c-ink`、法務細字 `--c-quiet`（小本文には使わずUI/補助に限定）。
**状態** … リンクは default（muted）/ hover（ink）/ focus（共通 outline）。現在ページに当たるリンクがあれば `aria-current` で示す。
**規則** … 02 Wurman：Footer は「最終の出口」。主要セクション・問い合わせ・法務へ確実に辿れる経路を置き、行き止まりを塞ぐ。07 抑制：装飾より到達性、巨大ロゴや過剰なリンク網を避け LATCH（Category）で整理。
**a11y** … `<footer>`（＝`contentinfo`）。リンク集合は `<nav aria-label="フッター">`。カラム見出しは見出し要素で構造化。低コントラストの細字を本文サイズで使わない。
**関連** … Header / Navigation / Link / List。

---

### Breadcrumbs 〔Breadcrumb trail〕

**用途** … 階層内の現在地を「ルート → … → 現在ページ」のリンク列で示し、上位階層への最短の出口を与える。深い階層で迷子を防ぐ。
**変種** … 全階層表示 / 中間を「…」に省略（長い経路）/ モバイルは「← 親階層」1つに縮約。
**構成** … `nav` > `ol` > `li`（リンク）＋区切り（`/` や `›`、CSS生成）。最後の `li` ＝現在ページで**非リンク**。
**寸法** … 行高さ 44px 以上、項目と区切りの `gap:8px`、文字 14px 前後。区切り記号は装飾色 `--c-line-strong` で控えめに。
**色** … 中間リンク `--c-muted`→hover `--c-ink`。現在ページ（末尾）は非リンクの `--c-ink`（押せない見た目）。区切りは `--c-quiet`/`--c-line-strong`。
**状態** … 中間：default（muted）/ hover（ink）/ focus（共通 outline）。末尾：静的テキスト（hover/focus なし）。
**規則** … 02 Legibility：現在地（末尾）は必ず読め、かつ押せないことが見た目で分かる（Path＝来た経路の可視化）。Wurman：各上位はリンク＝いつでも戻れる出口、dead end を作らない。区切りだけで意味を担わせず順序は `ol` で保証。
**a11y** … `<nav aria-label="パンくず">` ＋ `<ol>`。現在ページの `li` に `aria-current="page"`（リンクにしない）。区切り記号は `aria-hidden` か CSS で挿入し読み上げに混ぜない。
**関連** … Navigation / Header / Tree view / Pagination。

---

### Tabs 〔Tabbed interface〕

**用途** … 同一文脈の複数パネルを同じ場所で切替え、選択中を明示する。画面遷移なしに関連ビューを行き来させ、出口を断たない。
**変種** … 下線型（underline）/ 囲み型（enclosed）/ セグメント風。スクロール可（多数タブ）。※URL に紐づくページ切替なら Tabs でなくナビゲーションを使う。
**構成** … `[role=tablist]` > 各 `[role=tab]`、対応する `[role=tabpanel]`。選択タブに下線/地の現在地マーカー。
**寸法** … タブのタッチ最小 44–48px、padding `8px 16px`、タブ間 `gap:8px`。下線型は選択タブ下に 2px の `--c-accent` ライン。
**色** … 非選択タブ `--c-muted`→hover `--c-ink`。選択タブ 文字 `--c-accent` ＋（囲み型は地 `--c-accent-sunk`）＋下線 `--c-accent`。
**状態** … default（muted）/ hover（ink）/ active＝選択中（accent＋マーカー）/ focus（共通 outline）/ disabled（quiet）。
**規則** … 02 Legibility：選択中タブを色だけでなく下線/地でも示す（色覚非依存）。03 Norman：タブ＝同一場所での内容差し替えという conceptual model を守り、パネルは隣接配置で因果を切らない。判断材料（各パネルの内容）を畳んで失わせない。
**a11y** … `tablist`/`tab`/`tabpanel`、選択タブ `aria-selected="true"` ＋ `tabpanel` を `aria-labelledby` で結ぶ。矢印キーでタブ間移動、Enter/Space で選択、Tab はパネルへ抜ける（ロービングtabindex）。
**関連** … Segmented control / Navigation / Accordion / Pagination。

---

### Pagination

**用途** … 大量の項目を複数ページに分割し、現在ページ・総数・前後への移動手段を示す。一覧の続きへ進む出口を保証する。
**変種** … 番号列（1…5）/ 前・次のみ / 「もっと読む」/ 無限スクロール併用。総件数・範囲（「21–40 / 320件」）を併記。
**構成** … `nav` > `ul` > `li`（ページ番号リンク・前/次・省略「…」）。現在ページは非リンクで強調。
**寸法** … 各ページャのタッチ最小 44–48px（数字は正方ボックス＋padding で確保）、項目間 `gap:8px`、radius `6px`。
**色** … 通常番号 `--c-muted`→hover 文字 `--c-ink`＋地 `--c-sunk`。現在ページ 文字 `--c-accent`＋地 `--c-accent-sunk`（非リンク）。無効な前/次は `--c-quiet`＋ `disabled`。
**状態** … default（muted）/ hover（ink＋sunk）/ active＝現在ページ（accent・非リンク）/ focus（共通 outline）/ disabled（端で前/次が quiet・操作不可）。
**規則** … 02 Tufte/Legibility：現在ページと総数（判断材料）を必ず示し、抑制を理由に件数を削らない。Wurman：先頭/末尾・前/次への経路で行き止まりを防ぐ。03 Norman：押下後どこへ来たかを現在ページ更新で即フィードバック。
**a11y** … `<nav aria-label="ページ送り">`。現在ページに `aria-current="page"`。番号リンクは `aria-label="3ページ目"` 等で明示、無効ボタンは `aria-disabled`／`disabled`。Enter/Space で実行。
**関連** … Navigation / Table / List / Breadcrumbs。

---

### Tree view

**用途** … 入れ子の階層（ファイル/組織/カテゴリ）を展開・折りたたみで提示し、現在選択中のノードを示す。深い構造を畳んで全体像と現在地を両立させる。
**変種** … 単一選択 / 複数選択（チェック）/ 遅延読込（子を開く時に取得）/ アイコン付き（フォルダ・ファイル）。
**構成** … `[role=tree]` > `[role=treeitem]`（入れ子は `[role=group]`）。各行に展開トグル（▶/▼）＋ラベル＋任意アイコン。インデントで階層深度を表現。
**寸法** … 行のタッチ最小 44px、1階層のインデント `16px`（spacing-4）。展開トグルは視覚 24px＋padding で当たり判定を確保、行内 `gap:8px`。
**色** … 通常ノード `--c-muted`/ラベル `--c-ink`、hover 地 `--c-sunk`。選択中ノード 地 `--c-accent-sunk`＋文字 `--c-accent`。トグル記号 `--c-quiet`。
**状態** … default / hover（sunk地）/ active＝選択中（accent-sunk）/ expanded・collapsed（トグル向きで明示）/ focus（共通 outline）/ disabled（quiet）。
**規則** … 02 Legibility：現在選択ノードを必ず読め、展開状態（開/閉）も記号で判別可能にする（District＝まとまりの可視化）。03 Norman：▶/▼ で開閉の signifier と mapping を一致。Wurman：展開の入口と親へ戻る出口を保ち、深い枝で行き止まりにしない。
**a11y** … `[role=tree]`、各 `treeitem` に `aria-expanded`（枝のみ）・`aria-selected`・`aria-level`。↑↓で項目移動、→で展開/子へ、←で折りたたみ/親へ、Enter/Space で選択。フォーカスは1要素（ロービングtabindex）。
**関連** … Navigation / Accordion / List / Breadcrumbs。
