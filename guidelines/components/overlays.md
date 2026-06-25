# オーバーレイ — コンポーネント詳細

本文の上に重ねて出す面。前景化のコストは高いので、**いつ覆うか・いつ覆わないか**を分けて設計する。共通規則（[components/README](./README.md#どのコンポーネントも継承する共通規則universal)）は満たした前提で、各部品の固有仕様だけを記す。

---

### Modal  〔Dialog, Popup〕

**用途** … 前面に出て応答を要求し、背後の操作を遮断する面。確認・破壊操作・必須入力など「先に片付けないと進めない」ときだけ。乱用すると割り込みが日常化し、本当に重要なときに効かなくなる。
**変種** … alert dialog（確認・破壊、2択）/ form dialog（入力）/ 全画面モーダル（モバイル）。
**構成** … backdrop ／ panel（ヘッダ：タイトル＋閉じる× ／ 本文 ／ フッタ：アクション群、主操作を右端）。
**寸法** … panel radius `16px`（golden-0 / `rounded-2xl`）。本文 padding `16px 24px`（カード比 1:1.5 / `py-4 px-6`）。最大幅 480–560px、viewport 端から最低 16px。フッタのボタンは radius `6px`（golden-2）。
**色** … panel = `--c-surface`、境界は影でなく `--c-line` ヘアライン。backdrop = 半透明の ink（`rgba(20,24,31,.5)` ≒ `--c-ink` 50%）。影は `shadow-sm` まで（Apple 機能的 Depth = 階層提示のみ。浮かせ装飾にしない）。
**状態** … 開（backdrop フェード＋panel を短く拡大/上昇）／ 閉（逆再生）／ 遷移中は背景を `inert`。`prefers-reduced-motion` で移動量を縮める。
**規則** … 03 Calm: 割り込みは**緊急かつ要応答**のときだけ。通常の更新・完了通知はモーダルにせず Toast や控えめなインジケータへ。 Apple: 開閉遷移は「どこから来てどこへ行くか」を伝える機能的 Depth に限る。 破壊操作は確認モーダルで毎回止めず **undo を優先**（`M-RECOVERABILITY` / Raskin）。背景に**フォーカストラップ**。
**a11y** … `role="dialog"` `aria-modal="true"`、`aria-labelledby` でタイトル参照。focus trap（Tab は panel 内で循環）／ 開いたら先頭操作 or panel へ focus ／ **Esc で閉じる** ／ 閉じたら**起動要素へ focus を返す**。backdrop クリックで閉じるのは非破壊時のみ。
**関連** … Drawer / Popover / Toast / Alert

---

### Drawer  〔Sheet, Flyout〕

**用途** … 画面の端からスライドして出るパネル。ナビ・フィルタ・詳細・設定など、現在の文脈を保ったまま副次面を開く。スライド方向そのものが「どの端から来たか」を伝える。
**変種** … side drawer（左右・ナビ/フィルタ）/ bottom sheet（モバイル・親指ゾーン）/ modal drawer（backdrop で背景遮断）/ non-modal（背景操作を残す persistent）。
**構成** … （modal時）backdrop ／ 端に接する panel ／ （sheet）ドラッグハンドル ／ ヘッダ ／ スクロール本文 ／ フッタ。
**寸法** … panel は**接する端の角丸を 0**、室内側の 2 隅のみ `16px`（golden-0）。本文 padding `16px 24px`。side は幅 320–400px、bottom sheet は内容高に追従。フッタ・操作は `safe-area-inset` を適用。
**色** … panel = `--c-surface` ＋ `--c-line`。modal drawer は半透明 ink backdrop、non-modal は backdrop なしでヘアラインのみで面を分ける。影は `shadow-sm` まで。
**状態** … 開（端からスライドイン＝出所を位置で提示）／ 閉 ／ ドラッグ追従（sheet）。reduced-motion でスライド距離短縮。
**規則** … Apple: スライド方向＝前後関係を伝える機能的 Depth/motion。 modal なら背景 `inert`＋focus trap、non-modal なら背景操作を残す（trap しない）。 10 Fitts: bottom sheet の主操作は下部親指ゾーンへ。 Calm: 常時開きっぱなしの persistent drawer は周辺情報に留め、注意を奪わない。
**a11y** … modal drawer は `role="dialog"` `aria-modal="true"`＋focus trap＋Esc＋**返り先 focus**。non-modal は trap しない。swipe-to-close には必ずキーボード等価（閉じるボタン）を併設。
**関連** … Modal / Navigation / Popover

---

### Popover  〔—〕

**用途** … トリガ要素をクリック/押下して、その**近くにアンカーして開く**小パネル。中にフォーム・リンク・選択などの**操作可能な要素**を置ける。Tooltip と違い操作可・focus が中へ移る。
**変種** … メニュー型 / 簡易編集フォーム型 / 詳細カード型。
**構成** … トリガ ／ パネル ／（任意）くちばし（矢印）／ 本文。
**寸法** … panel radius `10px`（golden-1。モーダルより一段小さい従属面）。padding `12–16px`（コンパクト）。トリガから 4–8px オフセットでアンカーし、viewport 端で自動反転（flip）。
**色** … `--c-surface` ＋ `--c-line` ヘアライン。**backdrop は持たない**（軽量・非モーダル、背景を覆わない）。影は `shadow-sm` まで（浮き＝前後関係の最小限）。
**状態** … 開（トリガ起点に短くフェード/スケール）／ 閉（外側クリック・Esc・トリガ再押下）／ トリガは `aria-expanded` で開閉を表す。
**規則** … 03 Norman: **クリックで開く**（hover で開かない＝操作可能ゆえ誤発火を避ける）。 Apple: トリガ位置にアンカーして mapping を保つ。 Calm: 背景を覆わず軽量に。応答必須・重い内容なら Modal へ格上げする（覆うコストを払う判断）。
**a11y** … トリガに `aria-haspopup` ＋ `aria-expanded`、操作可パネルは `role="dialog"`（menu 用途は `role="menu"`＋矢印キー）。開いたらパネル内へ focus 移動、focus はパネル内に留め、**Esc でトリガへ返す**。クリックアウトで閉じる。
**関連** … Dropdown menu / Tooltip / Modal

---

### Tooltip  〔Toggletip〕

**用途** … 要素の**補足説明**を一時表示する。Tooltip = hover/focus で自動表示（補助ラベル）。Toggletip = クリックで開く補足。いずれも**操作不可**・消えて困る重要情報やリンクを入れない。
**変種** … Tooltip（hover+focus・純説明）/ Toggletip（クリックトグル・`aria-live`）。
**構成** … トリガ（アイコン/テキスト）／ 小さなバブル ／（任意）くちばし。
**寸法** … radius `4–6px`（golden-3/2。最小面）。padding `4px 12px`〜`8px 12px`（タグ比 1:3 / `py-1 px-3`）。1–2行、最大幅 ≈240px。トリガから 4–8px オフセット、端で反転。
**色** … `--c-surface` ＋ `--c-line`、または反転（濃い `--c-ink` 地＋明色文字）。いずれもコントラスト本文 4.5:1 を満たす。影は使わない/最小。
**状態** … 表示（hover/focus in、遅延 0.1–0.3s）／ 非表示（hover/focus out、**Esc で即時**）。tooltip 本体には focus を移さない。
**規則** … 03/10: hover だけでなく **focus でも必ず出す**（キーボード・タッチで到達可能に）。 Calm: 純粋な補足に限る。操作・重要情報は入れない（消えて困る情報は本文へ）。 Apple Clarity: 曖昧アイコンの意味を Tooltip だけに頼らず、可視ラベル併用も検討。
**a11y** … トリガに `aria-describedby`（Tooltip）。Toggletip は本体を `button`、補足は `role="status"`/`aria-live` で読み上げ。WCAG 1.4.13: hoverable & dismissible（ポインタを乗せても一定時間維持、Esc で消せる）。
**関連** … Popover / Badge / Icon

---

### Toast  〔Snackbar〕

**用途** … 操作の結果や非緊急の通知を、前面の隅に**一時表示して自動消滅**させる。応答を要求しない（要求するなら Modal / Alert）。破壊操作には **undo 導線**を載せる。
**変種** … 通知のみ / アクション付き（undo・再試行）/ semantic（success・danger・info、色＋アイコン）。
**構成** … 隅のスタック容器 ／ アイコン ／ メッセージ ／（任意）アクション ／（任意）閉じる×。
**寸法** … radius `10px`（golden-1）。padding `12px 16px`〜`16px 24px`。画面隅から 16px ＋ `safe-area-inset`。複数は縦スタック＋8px 間隔（重ねない）。
**色** … `--c-surface` ＋ `--c-line`、semantic は text/bg/border の 3 役割（[color-system](../values/color-system.md)）。影は `shadow-sm` まで。
**状態** … 表示（端からスライド/フェード）／ 自動消滅（4–8s、hover/focus で一時停止）／ 手動 close。重要なら自動消滅させず残す。
**規則** … 03 Calm: **通常更新はモーダルにせず Toast で控えめに**。割り込みは緊急時のみ。 Raskin/`M-RECOVERABILITY`: 破壊操作の確認は確認モーダルでなく Toast の undo で（「削除しました｜元に戻す」）。undo を押せる十分な表示時間を取る。 `M-CRITICAL-VISIBILITY`: 重大エラー・期限は自動消滅させず、静けさに埋もれさせない。
**a11y** … 非緊急は `role="status"` `aria-live="polite"`、緊急は `role="alert"` `assertive`。focus を奪わない（作業を中断しない）が、アクションはキーボードで到達可能に。種別は色だけで示さずアイコン＋ラベルで二重化。
**関連** … Alert / Modal / Spinner
