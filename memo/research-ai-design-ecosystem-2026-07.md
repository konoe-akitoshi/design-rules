# 調査: AIデザイン知見エコシステム（2026-07）

3並列リサーチ（①AI向けガイドライン規約 ②評価・ベンチマーク手法 ③プロのデザインシステム知見）の原典アーカイブ。
既存カバレッジとの照合結果は末尾。**取り込みは guidelines/ / prohibited.md / tools/design-lint.py / ベンチ手順の各レイヤーへ差分のみ**。

---

## ① AI向けデザインガイドラインの規約・慣行

### DESIGN.md — 新興標準
- 仕様: https://github.com/google-labs-code/design.md（Google Labs、2026-04）
- コレクション: https://github.com/voltagent/awesome-design-md / https://designmd.app/
- 構造 = YAML frontmatter（機械可読トークン＝規範値）+ Markdown 本文（意図・根拠）。
- frontmatter: `name`(必須)/`version`/`colors`/`typography`/`rounded`/`spacing`/`components`。トークン参照は `{colors.primary}` ドット記法。
- 本文固定順: Overview → Colors → Typography → Layout & Spacing → Elevation → Shapes → Components → **Do's and Don'ts**。
- `npx @google/design.md lint` がコントラスト比・構造整合を機械検証。「検証可能なルールは構造化スペックへ、判断系は自然言語のまま」という分離思想。
- 三層モデル: AGENTS.md=振る舞い / SKILL.md=タスク / DESIGN.md=外観。

### Rauno Freiberg — Web Interface Guidelines
https://interfaces.rauno.me/ / https://github.com/raunofreiberg/interfaces
- 入力は `<form>` で包み Enter 送信可。`type`/`autocomplete` を意味的に正しく。
- 送信後ボタン disable（二重送信防止）。トグルは確認なしで即時反映。
- font-weight 400 未満を使わない。hover/選択で weight を変えない（シフト）。
- `tabular-nums` を表・タイマーに。`clamp()` で流体フォント。
- インタラクションのアニメは 200ms 以下。テーマ切替時は transition 無効化。高頻度操作にアニメ禁止。画面外ループアニメ停止。
- hover は `@media (hover: hover)` 限定。入力は 16px 以上（iOS ズーム防止）。タッチで autofocus しない。
- 大きな `blur()` 回避。`will-change` はアニメ中のみ。
- disabled ボタンにツールチップ禁止。アイコンのみ要素に `aria-label`。focus ring は box-shadow（角丸追従）。
- 楽観的更新+エラー時ロールバック。フィードバックはトリガー近くにインライン。空状態は作成アクション+テンプレ提示。
- リスト項目間デッドスペースを padding 拡大で排除。

### Vercel — web-interface-guidelines（AIに貼る前提の初メジャー）
https://vercel.com/design/guidelines / https://github.com/vercel-labs/web-interface-guidelines
- 全ルール MUST/SHOULD/NEVER の1行命令形。8セクション。
- ヒットターゲット最小24px、モバイル44px。視覚が小さければ不可視ヒット拡張。
- NEVER: paste ブロック / ズーム無効化 / `<div onClick>` ナビ / outline を代替なしで除去。
- フォーム: エラーはフィールド隣インライン+送信時に最初のエラーへフォーカス。スピナー表示時のみ disable。未保存変更でナビ警告。末尾空白トリム。
- **URL が状態を反映**（フィルタ/タブ/ページネーション/展開をディープリンク可能に）。Back/Forward でスクロール復元。
- アニメは compositor プロパティ（transform/opacity）のみ。**NEVER `transition: all`**。layout プロパティをアニメしない。reduced-motion 必須。中断可能。
- skeleton は最終レイアウトと同形。empty/sparse/dense/error 全状態を設計。行き止まり禁止。
- `Intl.DateTimeFormat`/`NumberFormat`。`…` は文字実体。`10&nbsp;MB`。
- flex 子の truncation に `min-w-0`。50項目超は仮想化。画像は寸法明示（CLS）。ミューテーション500ms以内。
- ダークは `<html>` に `color-scheme: dark`。ネイティブ `<select>` に背景・文字色明示。
- 影はレイヤード（ambient+direct）、ボーダー/影は半透明。入れ子角丸は子≤親で同心円。コントラストは APCA 推奨。hover/active/focus でコントラスト上げる。

### Vercel — Teaching agents product design（ルール運用の方法論）
https://vercel.com/blog/teaching-agents-product-design-at-vercel
- **観測可能な決定だけをルール化**（"Buttons should be clear" は不可、"Destructive actions use Verb+Noun" は可）。
- 決定論的チェック（linter）と判断系ガイダンス（skill）を分離。ルール追加には根拠・スコープ・例外・正誤両実例を要求。
- 例: 静的2–3択は select でなく radio / ネストモーダル禁止 / 4px グリッド外をフラグ / className でコンポーネントの color・radius・shadow 上書き禁止。

### ibelick/ui-skills（baseline-ui、deslop 代表格）
https://github.com/ibelick/ui-skills
- MUST: 見出し `text-balance`・本文 `text-pretty`、データに `tabular-nums`、アイコンのみボタンに `aria-label`。
- NEVER: paste ブロック / layout プロパティのアニメ / 大面積 blur・backdrop-filter のアニメ / アニメ外の `will-change`。
- `h-screen`→`h-dvh`、fixed に safe-area-inset、破壊操作に AlertDialog、構造的 skeleton。
- entrance は `ease-out`、フィードバック最大200ms。「要求されない限りグラデ禁止」「1ビューにアクセント1色」。

### Anthropic frontend-design スキル / frontend_aesthetics cookbook
https://claude.com/blog/improving-frontend-design-through-skills / https://platform.claude.com/cookbook/coding-prompting-for-frontend-aesthetics
- **AI収束3類型の名指し禁止**: ①クリーム地(#F4F1EA近傍)+高コントラストセリフ+テラコッタ ②ほぼ黒地+アシッドグリーン/朱の単一アクセント ③hairline罫線+radius 0 の新聞風。「これらは選択ではなくデフォルト」。
- 2パス強制: 先にトークン系（色4–6・書体2+ロール・ASCIIワイヤー・**signature=記憶される唯一の要素**）を計画→自己検査→合格後のみコード。
- 回避フォント: Inter/Roboto/Open Sans/Lato/Arial/system。代替は方向別（JetBrains Mono、Playfair/Fraunces、Clash Display/Satoshi、IBM Plex、Bricolage Grotesque…）。
- **ウェイトは両極端（200 vs 800）。サイズジャンプは3倍以上**。支配色+鋭いアクセント > 均等パレット。
- モーションは散発 micro-interaction より **1回の演出されたページロード（staggered reveal）**。
- 文言: 能動態、「Save changes」であって「Submit」でない。「Publish」→トースト「Published」の語彙一貫。エラーは謝らず原因+修正法。
- 大胆さは1箇所に集中、残りは静かに。番号マーカーは実順序があるときだけ。

### 背景分析
- 紫収束の起源 = Tailwind UI の `bg-indigo-500` が訓練データを汚染（Adam Wathan が 2025-08 に言及）。
- **ネガティブ制約（何を書かないかの指定）が最も費用対効果が高い**が2025-26の定着認識。
- Figma Make 公式の書き方指針: 曖昧より命令形／**長い1ファイルより短い多ファイル**（progressive disclosure）。

---

## ② 評価・ベンチマーク手法

### アリーナ型
- **Design Arena** https://www.designarena.ai/ — 4モデル5戦トーナメント→Bradley-Terry。既知バイアス:「投票者は要件を知らず綺麗さに流れる」。
- **WebDev Arena** — **preference-10k データセット公開**（HuggingFace: lmarena-ai/webdev-arena-preference-10k、1万件の実投票+コード）。
- **UI-Bench** (arXiv 2508.20410) — 専門家4,000+判定、TrueSkill+信頼区間。**30プロンプトの公開セット**は自前ベンチ題材に流用可。

### 自己批評ループ
- **Anthropic ハーネス設計記事** https://www.anthropic.com/engineering/harness-design-long-running-apps
  - generate → render → 評価者が自律操作 → critique → refine、1世代 5–15 イテレーション。
  - ルーブリック4軸: Design Quality / **Originality（脱テンプレ・重み付け対象）** / Craft / Functionality。Claude は Craft/Functionality が元々強いので Originality に重み。
  - few-shot 採点例で較正。ルーブリックの語彙自体が出力を形成する。生成側に「不調なら戦略的ピボット」を明示。
- **Justin Wetch のスキル改善検証** https://www.justinwetch.com/blog/improvingclaudefrontend
  - 50プロンプト × 新旧 × Puppeteer スクショ → 匿名化ブラインド対比較（Opus判定）。75%勝率 p=0.0125。
  - 5軸: Prompt Adherence / Aesthetic Fit / Visual Polish / UX / Creative Distinction。
  - 知見: 「世代間で収束するな」は記憶が無いので不可能 →「最初に浮かんだ凡庸な選択に安住するな」へ書換え。禁止と推奨を **INSTEAD ペア**で。曖昧形容詞を実行可能指示へ。美的方向語彙の列挙で探索空間拡張。

### 論文
- **WebGen-V** (arXiv 2510.15306) — **セクション単位評価が全ページ総評に勝る**（欠陥検出 F1 0.78 vs 0.46）。9メトリクス: Text(正確性/配置/可読性) Media(整合/位置/寸法) Layout(**重なり/整列/gap一貫性**)。低スコアセクションのみ再生成。
- **ArtifactsBench** (arXiv 2507.04952) — タスク毎の細粒度チェックリストで MLLM 判定を拘束+二審制。人間選好と94%相関。
- **Design2Code** (arXiv 2403.03163) — 参照比較: テキストマスク後 CLIP 類似度 + ブロックマッチ（面積/Sørensen-Dice/CIEDE2000/位置）の診断分離。

### 機械 lint
- **Project Wallace** https://www.projectwallace.com/ (`@projectwallace/css-analyzer`) — CSS から全色・font-size・shadow・spacing を抽出し**ユニーク値数＝トークンドリフト検出**。
- axe-core `target-size` / Lighthouse tap-targets（48dp+8px）。自動検出は a11y 問題の30–40%が限界という通説。
- stylelint/ESLint で任意値（`p-[13px]`、`text-[#hex]`）フラグ。

### プロダクトチームのレバー
- **v0**: shadcn/ui+Lucide に部品固定（探索空間を絞る）、「指定なき限り indigo/blue 禁止」「セマンティック変数色のみ」。
- **Lovable**: 「The design system is everything」— 直接色クラス（`text-white`/`bg-black`）禁止、全て CSS 変数化、**デザインシステム定義が先・コンポーネントは後**。
- **Figma Make**: ユーザー編集可能な System Guidelines、命令形・短文・多ファイル。

---

## ③ プロのデザインシステム知見

### Geist（最重要: スケール段=意図）
https://vercel.com/design.md / https://vercel.com/geist/colors
- カラー10段: 100=bg / 200=hover bg / 300=active bg / 400=border / 500=hover border / 600=active border / 700=solid塗り / 800=solid hover / 900=二次text / 1000=一次text。
- **状態遷移 = スケール導出: hover=+1段、active=+2段**。hover 色を手で選ばない。
- gray と gray-alpha（border/divider/overlay 用半透明）を別スケールで。
- スペーシングリズム: **グループ内8 / グループ間16 / セクション間32–40**。カード padding 24（標準）/16（コンパクト）/32（ヒーロー）。
- 角丸: 6=コントロール / 12=メニュー・モーダル / 16=フルスクリーン面 / 9999=ピル。
- シャドウ実値3段（カード `0 2px 2px rgba(0,0,0,0.04)` 等、レイヤード）。
- モーション: デフォルト0ms / 状態~150 / ポップオーバー~200 / モーダル~300。
- focus ring: `0 0 0 2px #fff, 0 0 0 4px #006bff`。ボタン高 32/40/48。
- 文言: 動詞+名詞（`Deploy Project`）、`Confirm`/`OK`/裸動詞禁止。トーストは "successfully" 禁止・ピリオドなし。進行中=現在分詞+`…`。

### Stripe / Linear
- Stripe: ディスプレイ層は常に weight 300。シャドウ色は黒でなくブランド紺 `rgba(50,50,93,0.25)`。**6マイクロステート必須**: default/hover/focus/active/disabled/loading。
- 共通: 書体1ファミリー・4–6段 / 金額は tabular / ヘアライン0.5–1px低不透明 / 「インタラクション密度は高く、視覚密度は低く」/ skeleton は実レイアウト一致（汎用スピナー禁止）。
- Linear: アクセントは1画面につき主要アクション1つ。カードは塗りでなく 1px inset ボーダー+ソフトシャドウ。

### タイポ・色の職人知識
- 行長 **45–75字・理想66字 → `max-width: 66ch`**（px 固定は WCAG 1.4.4 で破綻）。行間は行長連動: 基準1.5、75字超なら1.6–1.7、見出し1.1–1.2。
- 光学サイズ: `font-optical-sizing: auto`、~19px以下=Text カット / 20px以上=Display カット（Apple 式）。
- Utopia 流 fluid scale: 小画面スケールと大画面スケールを clamp 補間、**スペーシングも同一ロジックで導出**。https://utopia.fyi/
- **OKLCH ランプ**: hue 固定・L=10–90% 10%刻み・chroma ランプ内一定。ガマット外は L より先に C を削る。60-30-10。導出はコードで: `oklch(from var(--brand) calc(l*0.9) c h)`、`color-mix(in oklab, …)`。**2つ目の hex を手で置かない**。
- **APCA 閾値**: Lc 90=本文推奨 / 75=本文最低(16px/500) / 60=非本文 / 45=大見出し / 30=placeholder・disabled / 15=非テキスト下限。明暗テーマで同値が同可読性（WCAG2 比の最大利点）。
- **ダーク導出**: 背景 L8–12%・純黒禁止。text #E0E0E0–#F0F0F0（純白は眩輝）。**エレベーション=明度+5–8%/段**。彩度: 青系−20–30% / 赤橙−10–15% / 緑は−＋3–5°ティールへ。アクセントは hue 固定 L50→60%。
- AI が最も外すのはダークモードの spacing という指摘あり。

### AIスロップ16パターン（prohibited 増補材料）
https://www.developersdigest.tech/blog/ai-design-slop-and-how-to-spot-it
- 未カバー分: H1 上のバッジ/ピル / 統計バナー行 / 「1,2,3ステップ」セクション / Inter 見出し中1語だけ serif italic / 定番コンボ（Space Grotesk+Instrument Serif）/ 色付きグロー / 絵文字アイコンのナビ / 全大文字見出しのデフォルト化。
- 核心: 生成前に「パレット・書体システム・主レイアウトプリミティブ1つ」を決めてから一貫強制。

### モダン CSS の when-to-use
- コンテナクエリ: ブレークポイントは「ラベルが折り返す幅」などコンポーネント都合で。`container-type: inline-size` と `subgrid` は同一要素で共存不可。
- `:has()`: 「画像を含むカードはレイアウト切替」「エラー入力を含むグループの装飾」。
- subgrid: カードグリッドの行揃え。Flex=部品内 / Grid=構造 / Subgrid=入れ子整列。
- **`text-wrap: balance`=h1–h4（孤立語防止）/ `pretty`=本文段落** — 機械ルール化可。
- `light-dark()` + `color-scheme: light dark` でテーマ二重定義排除。
- View Transitions（Baseline 2025-10）: 同一要素の連続性を見せる時のみ。
- スクロール駆動アニメ: `animation-timeline: view()/scroll()`。必ず reduced-motion 内。スクロール連動スプリング禁止。

---

## 照合結果 — 既にカバー済み（重複取り込み不要）

- 非対称 padding / 入れ子角丸（同心円）/ テンプレ骨格禁止 / eyebrow / 1アクセント+セマンティック / タッチターゲット3層 / focus 可視 / 色のみ依存禁止 / ダークランプ基本 / 全長・完全性の床 / トークン SSOT / 決定順プロセス / lint レイヤーの存在自体。
- 本リポジトリの構成（tokens SSOT + 決定順 + prohibited + design-lint）はエコシステムの最先端4点セット（トークン/プロセス/ネガティブ制約/機械検証）と一致。取り込みは差分のみで良い。
