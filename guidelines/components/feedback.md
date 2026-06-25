# フィードバック・状態 — コンポーネント詳細

システムの状態・進捗・結果をユーザーに返す部品群。注意の階層を守りつつ、重大な変化と次の行動だけは確実に届ける（[03](../03-interaction-feedback.md) / [08](../08-states-resilience.md) / [10](../10-accessibility.md)）。

---

### Alert 〔Banner, Callout, Inline message〕

- **用途**：状態の重要な変化・前提・結果をその場で目立つ形で知らせる。一時表示は Toast（→ [overlays](./overlays.md)）、補足は Callout。
- **変種**：`info` / `success` / `warning` / `danger`。配置で inline（フォーム直上等）／ page banner（画面上部の帯）。任意で dismiss（閉じる）。
- **構成**：先頭アイコン ＋ 見出し（任意）＋ 本文 ＋ アクション（再試行・詳細・取消等）＋ 閉じるボタン（任意）。
- **寸法**：page banner は非対称padding `32px 48px`（block:inline = 1:1.5、`asymmetricPadding.banner`）、inline は `16px 24px`。radius は `golden.1`(10px)。アイコンと本文の gap `8px`。閉じるボタンは当たり判定 `44px`。
- **色**：地は `--c-*-bg`、左の意味は `--c-*-border`（全周ヘアライン。`border-t-4` のカラーバー禁止）、アイコン/見出しは `--c-*`(text)。success=`--c-success`、warning=`--c-warning`、danger=`--c-danger`、info=`--c-accent`。**色＋アイコン＋ラベルで二重化**し、彩度を上げない。
- **状態**：static（表示）/ dismissible（hover で閉じるボタン強調 → 消滅）/ アクション付きは button 状態を継承。
- **規則**：03 Cybernetics — エラー Alert は「何がどう違うか（検出）」＋「どう直すか（復旧導線＝再試行/設定/問い合わせ）」をセットで出す（コードだけで放置しない）。03 Calm — 割り込みは緊急かつ行動が必要なときだけ。常時赤バナーを出さない。ただし重大なエラー・期限は静けさを理由に埋もれさせない（`M-CRITICAL-VISIBILITY`）。コピーは責めず能動態（「不正な値」→「日付は YYYY-MM-DD で入力してください」）。
- **a11y**：危険・即応は `role="alert"`＋`aria-live="assertive"`、情報・成功は `role="status"`＋`aria-live="polite"`。動的に現れる Alert に限り live region を使う。アイコンは装飾なら `aria-hidden`、意味は本文で担保。閉じるは `<button aria-label="閉じる">`。
- **関連**：Toast / Toast との使い分け（恒常 vs 一時）、Empty state、Badge。

---

### Badge 〔Tag, Chip, Label, Pill〕

- **用途**：対象に付随する状態・属性・分類・件数を小さく示す。Badge=状態/件数（受動的表示）、Tag/Chip=分類・選択（操作可なことがある）。
- **変種**：意味色付き status badge（info/success/warning/danger/neutral）、件数 count badge（数値）、削除可能 chip、選択 filter chip。
- **構成**：（任意アイコン/ドット ＋）短いラベル。chip は任意で末尾に削除 `×`。
- **寸法**：非対称padding `4px 12px`（1:3、`asymmetricPadding.tag`）、radius `golden.3`(4px)（pill 形は全高 radius）。フォントは本文より小・行間詰め。操作可能 chip は当たり判定 `44px`＋間隔 `8px`。
- **色**：status は `--c-*-bg`＋`--c-*`(text)＋必要なら `--c-*-border`。neutral は `--c-sunk`＋`--c-muted`。**色のみに頼らずラベル文字を必ず持たせる**（点だけ・色だけのバッジ禁止）。`--c-quiet` は小さい文字に使わない（コントラスト不足）。
- **状態**：static（表示のみ）/ interactive chip は hover `sunk`・selected `accent-sunk`＋文字 `accent`・focus リング・removable は `×` に hover。
- **規則**：03 Calm — 常時点灯の赤バッジで注意を消耗させない。強調は変化のあった対象だけに絞る。08 — 「未確定/処理中」を確定済みに見せない（下書き/保存中/保存済みをラベルで区別）。10 — 状態の意味は色＋テキストで二重化。
- **a11y**：意味を持つバッジはテキストでも読めるようにする（例 `<span class="visually-hidden">状態: </span>進行中`）。件数バッジは `aria-label="未読 3件"`。装飾ドットは `aria-hidden`。削除 `×` は `aria-label="タグを削除"`。
- **関連**：Alert、Avatar（→ [display](./display.md)）、Filter（chip フィルタ）、Tooltip。

---

### Progress bar 〔Progress, Determinate progress〕

- **用途**：現在値／全体が分かる連続的な進捗を帯で示す（アップロード・処理・残ステップ）。割合不明なら Spinner を使う。
- **変種**：determinate（0–100%）/ indeterminate（不定。無限アニメ）/ ラベル付き（% や「3/10」併記）。
- **構成**：トラック（背景）＋フィル（進捗）＋任意ラベル（割合・残量・推定時間）。
- **寸法**：高さ `4–8px`、radius は高さの半分（pill）。トラックとラベルの gap `8px`。コンテナ幅いっぱい。
- **色**：トラック `--c-sunk`、フィル `--c-accent`。完了で `--c-success`、失敗で `--c-danger` に切替え可。ラベルは `--c-muted`。グラデーション/強い影で持ち上げない。
- **状態**：active（進行）/ complete（100%・色で完了）/ error（停止＋原因）/ indeterminate（待機）。
- **規則**：08 Cybernetics — 非同期処理は「いま動いている」ことを即時可視化し、進捗・推定時間で無反応と区別する。長い処理ほど残量や内容（「3/10 ファイル」）を見せる。08 — 失敗時は帯を赤にするだけでなく原因＋再試行を併記（→ Alert）。03 — 結果は同じ文脈で確認できるようにする（別画面に飛ばさない）。
- **a11y**：`role="progressbar"`＋`aria-valuenow`/`aria-valuemin`/`aria-valuemax`、indeterminate は valuenow を省く。完了・失敗は `aria-live="polite"` で通知。割合は文字でも提示し色だけにしない。
- **関連**：Spinner、Skeleton、Progress indicator（Stepper）、File upload（→ [forms](./forms.md)）。

---

### Progress indicator 〔Stepper, Steps, Wizard〕

- **用途**：複数手順のフロー（登録・チェックアウト・設定）で離散ステップの進行と現在地を明示する。連続割合は Progress bar。
- **変種**：水平／垂直、番号付き／アイコン付き、ラベルあり／なし、リニア（順送り）／非リニア（任意移動可）。
- **構成**：ステップ（番号/アイコン ＋ ラベル）＋接続線 ＋現在地マーカー。状態＝完了/現在/未到達/エラー。
- **寸法**：ステップ円は当たり判定 `44px`（操作可時）、円の gap `8px`、ラベルとの間 `4–8px`。マーカー radius は円。コンテナ `golden.1`。
- **色**：完了=`--c-success` or `--c-accent`、現在=`--c-accent`（地 `accent-sunk`）、未到達=`--c-line`＋文字 `--c-quiet`、エラー=`--c-danger`。接続線は `--c-line`、完了区間は accent。**現在地を色だけでなく太さ/塗り/番号で示す**。
- **状態**：complete / current（active 強調）/ upcoming（disabled 風・薄い）/ error（該当ステップを赤＋メッセージ）。
- **規則**：03 Norman — 現在地（観測）と残り（判断材料）を常に見せ、recognition over recall。M-JUDGMENT-MATERIAL に従い「今どこ・あといくつ」を削らない。08 — 中断・再開を許容し、入力済みステップを保持する。エラーは該当ステップに原因＋戻り導線を付ける。03 Calm — 現在ステップだけを強調し全点灯にしない。
- **a11y**：`<ol>` ベース、現在は `aria-current="step"`。各ステップ状態をテキストで（「ステップ2/4・完了」）。クリック移動可ならネイティブ `button`/`a` でキーボード到達。色＋形＋テキストで状態二重化。
- **関連**：Progress bar、Breadcrumbs / Tabs（→ [navigation](./navigation.md)）、Form。

---

### Spinner 〔Loader, Activity indicator, Throbber〕

- **用途**：割合が不明な短い処理中・操作不可を示す（送信中・読込中）。長い処理や割合が分かるものは Progress bar、初期レイアウト読込は Skeleton。
- **変種**：サイズ（小=ボタン内16px／中=領域24–32px／大=全画面）、inline／中央オーバーレイ。任意の補助ラベル。
- **構成**：回転インジケータ ＋任意ラベル（「読み込み中…」「保存中…」）。
- **寸法**：直径 16/24/32px、ストローク `2–3px`、ラベルとの gap `8px`。ボタン内蔵時はラベル幅を確保しレイアウトを飛ばさない。
- **色**：インジケータは `--c-accent`（ボタン内は `--c-on-accent`）、トラック相当は `--c-line`。`prefers-reduced-motion` で回転を抑え静的インジケータ＋テキストに退避。
- **状態**：loading（表示・対象を `aria-busy`／操作不可に）/ 完了で除去し結果を同じ文脈に反映。3秒超が見込まれるなら推定時間や内容を添える。
- **規則**：08 Cybernetics — 「いま動いている」ことを即時可視化し無反応に見せない。Human-Centered — 「送信中」を「送信完了」に見せない（処理中と確定を区別）。03 Calm — 平常の常時アニメにしない。スピナーは処理中のみ。長時間は Skeleton/Progress に切替える。
- **a11y**：装飾 SVG に**代替テキスト**を必ず付ける（`role="status"`＋可視 or `visually-hidden` の「読み込み中」）。`aria-live="polite"`。対象領域に `aria-busy="true"`。色だけで状態を伝えない。
- **関連**：Progress bar、Skeleton、Button（送信中状態）、Toast。

---

### Skeleton 〔Skeleton loader, Placeholder, Ghost〕

- **用途**：初期読込中、実コンテンツの代わりに灰色のプレースホルダを置き、構造を先に見せて体感待ち時間を下げる。短い処理や操作直後は Spinner。
- **変種**：テキスト行・見出し・アバター円・画像矩形・カード一式。shimmer（流れる光）あり／なし。
- **構成**：実レイアウトと同じ位置・サイズのブロック群（行・円・矩形）。**本物のレイアウトに正確に合わせ、表示後にガタつかせない**。
- **寸法**：ブロック radius は対象に合わせる（テキスト `golden.4`(2px)〜`golden.3`、画像/カードは実物の radius）。行間・余白は実コンテンツのトークンと一致（4ptグリッド）。
- **色**：ベース `--c-sunk`、shimmer は `--c-sunk`→`--c-line` の淡い移動。彩度・コントラストを上げない（注意を引かない）。
- **状態**：loading（表示）→ データ到着で実コンテンツに差し替え（レイアウトシフトを起こさない）。長すぎる場合や失敗時は error 表示（→ Alert）へ移行。
- **規則**：08 — loading は「処理中であること」を示しレイアウトを飛ばさない（CLS 回避）。固定件数を前提にせず、想定件数ぶんのスケルトンを出す。09 motion — shimmer は控えめ・短く、`prefers-reduced-motion` で停止。03 Calm — 過剰に動かさない。
- **a11y**：プレースホルダ自体は `aria-hidden="true"`、領域に `aria-busy="true"` を付け、別途 `role="status"` で「読み込み中」を伝える。装飾要素なので読み上げ対象にしない。
- **関連**：Spinner、Progress bar、Card / List / Table（→ [display](./display.md)）。

---

### Empty state 〔Blank state, Zero state〕

- **用途**：表示すべきデータが0件のとき、空白で放置せず「何が表示される場所か」＋「最初の一手」へ誘導する（invitation）。検索0件・初回・全削除後など。
- **変種**：first-use（初回・未作成）／ no-results（検索/フィルタ該当なし）／ cleared（完了・全消化）／ error 由来の空（→ 原則 Alert 寄り）。
- **構成**：軽いイラスト/アイコン（任意）＋見出し（状況）＋短い説明 ＋主アクション（作成/インポート/フィルタ解除）。
- **寸法**：コンテナは中央寄せ、内側 `32px` 前後の余白、要素間 `16px`、ボタンは非対称padding `12px 20px`／radius `golden.2`。アイコンは控えめサイズで主役にしない。
- **色**：地 `--c-surface`、見出し `--c-ink`、説明 `--c-muted`、主アクションのみ `--c-accent`。イラストは低彩度（注意を奪わない）。エラー由来でなければ赤/危険色を使わない。
- **状態**：no-results は条件提示＋「フィルタ解除」、first-use は作成導線、cleared は達成を肯定。loading 中は Skeleton、失敗は error 表示に分岐。
- **規則**：08 — empty/loading は次の行動を促す（invitation）。空＝行き止まりにしない。03 Norman — コピーは責めず能動態で次の一手を示す（「データがありません」だけで終えない）。M-PRAGMATISM — 文脈に応じ最も有効な一手を1つに絞る（CTA を増やしすぎない）。権限が理由なら理由＋申請先を出す（→ permission、Alert）。
- **a11y**：見出しは適切な heading レベル、主アクションはネイティブ `button`/`a`。検索後に動的表示するなら `role="status"`＋`aria-live="polite"` で件数0を伝える。アイコン/イラストは `aria-hidden`、意味はテキストで。
- **関連**：Alert（permission/error）、Skeleton、Button（→ [actions](./actions.md)）、Search（→ [forms](./forms.md)）。
