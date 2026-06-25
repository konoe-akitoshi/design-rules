# フォーム入力 — コンポーネント詳細

原則（[03](../03-interaction-feedback.md)/[07](../07-restraint-form.md)/[10](../10-accessibility.md)）をフォーム系部品へ落とした実用仕様。共通規則（[README の universal](./README.md#どのコンポーネントも継承する共通規則universal)）は前提とし、ここでは繰り返さない。値は [tokens.json](../../tokens.json) / [color-system](../values/color-system.md) を正とする。

---

### Text input  〔—〕

**用途** 1行のテキストを入力する（名前・メール・URL・検索語以外の短文）。`type` で用途を最適化する。
**変種** text / email / url / tel / password / number。password は表示切替トグルを末尾に併設。number は Stepper 併用可。
**構成** ラベル＋（補助テキスト）＋入力枠＋（先頭/末尾アイコン・単位）＋（エラーメッセージ）。
**寸法** padding `8px 16px`（py-2 px-4, formField 1:2）、radius 6px（rounded-md, golden L2）、高さは最小44pxを確保（py-2 で不足するなら縦padding増 or min-height）。アイコンと文字の間隔 spacing-2（8px）。
**色** 枠 `--c-line`／地 `--c-surface`／入力文字 `--c-ink`／placeholder `--c-quiet`／補助 `--c-muted`。focus 枠 `--c-accent`。エラー時 枠 `--c-danger-border`・文字 `--c-danger`・補助地 `--c-danger-bg`。
**状態** default / hover（枠 `--c-line-strong`）/ focus / disabled（地 `--c-sunk`・文字 `--c-quiet`）/ error / 読込（末尾 spinner、入力値は維持）。
**規則** 入力制約は placeholder でなく補助テキスト・例で事前提示する（03 Norman、placeholder は入力すると消えるためヒント単独は不可）。エラーは原因＋直し方を能動態で（「無効な値」ではなく「メールは name@example.com の形式で」, 03）。マイクロコピーは sentence case。
**a11y** `<input>`＋`<label for>` 必須。補助・エラーは `aria-describedby`、エラー時 `aria-invalid="true"`、必須は `aria-required`（記号も併記し色だけにしない, 10）。枠コントラスト 3:1。
**関連** Textarea / Label / Form / Search input / Stepper。

---

### Textarea  〔Text box〕

**用途** 複数行のテキストを入力する（コメント・説明・本文）。リサイズ可。
**構成** ラベル＋補助＋複数行枠＋（文字数カウンタ）＋（縦リサイズハンドル）。
**寸法** padding `8px 16px`（py-2 px-4）、radius 6px、最小高さは3〜4行（おおよそ88px〜）。`resize: vertical`（縦のみ許可）。
**色** Text input と同じ役割割当。カウンタは `--c-quiet`、上限超過時 `--c-danger`。
**状態** default / hover / focus / disabled / error / 上限接近（残数を警告色で予告）。
**規則** 横リサイズは行長を壊し可読性を下げるため禁止し、縦のみ許す（02 可読性 / 07 抑制）。上限があるなら残り文字数を常時可視化する（03 Cybernetics: 観測）。エラーは責めず直し方を示す。
**a11y** `<textarea>`＋`<label for>`。`maxlength` と残数を `aria-describedby` で結び、超過は `aria-live="polite"` で通知。focus 可視・最小タッチを満たす。
**関連** Text input / Rich text editor / Form。

---

### Label  〔Form label〕

**用途** 入力欄が何を求めるかを示し、必須/任意を明示する。
**構成** ラベルテキスト＋（必須/任意マーク）＋（補助の小テキスト）。
**寸法** 入力枠の直上に配置、下マージン spacing-1〜2（4–8px）。クリックで対象へ focus が移るので実質の操作面を広げる。
**色** 文字 `--c-ink`（読める下限を優先し muted/quiet に落とさない）、補助 `--c-muted`、必須マークは記号＋（色 `--c-danger` は補助）。
**規則** 必須は「※」「必須」など記号・語で示し、色だけに依存しない（10 色覚多様性）。placeholder でラベルを代替しない（消えると何の欄か不明になる, 03 Norman）。文言は能動態・sentence case・簡潔に。
**a11y** `<label for="id">` で入力と必ず紐付ける（暗黙の入れ子も可）。必須は視覚記号＋ `aria-required`。クリックで対象が focus されること。
**関連** Text input / Fieldset / すべてのフォーム入力。

---

### Fieldset  〔—〕

**用途** 関連する複数の入力（住所一式・ラジオ群など）を1つのまとまりとして括る。
**構成** 枠（fieldset）＋見出し（legend）＋内部の入力群。
**寸法** 内側 padding はカード基準 `16px 24px`（1:1.5）を上限、入力間は spacing-4（16px）。区切りは影でなくヘアライン `--c-line`（07）。枠 radius 10px（L1）で内部入力（6px）より大きく保つ（入れ子角丸 `R_inner = R_outer − padding`）。
**色** 枠 `--c-line`／legend `--c-ink`／地 `--c-surface`。
**規則** グループ化は Norman の概念モデルを助ける——意味的に関係するものだけを括る（02 構造）。装飾枠を多重にしない（07 抑制）。
**a11y** `<fieldset>`＋`<legend>` を使う（ラジオ/チェック群では legend がグループ名として読み上げられ必須）。legend は簡潔に。
**関連** Radio group / Checkbox / Form / Label。

---

### Form  〔—〕

**用途** 入力をまとめ、検証して送信する単位。送信前検証・送信中状態・結果通知を担う。
**変種** インライン検証（blur 時）／送信時の一括検証。
**構成** フィールド群（Fieldset/Label/入力）＋（全体エラーサマリ）＋送信ボタン＋（キャンセル）。
**寸法** フィールド間 spacing-4（16px）、セクション間 spacing-8（32px）。ボタンは padding `12px 20px`（py-3 px-5）。主操作（送信）はフォーム末尾、モバイルは親指ゾーンへ。
**色** エラーサマリは地 `--c-danger-bg`＋枠 `--c-danger-border`＋文字 `--c-danger`。送信中ボタンは spinner＋ラベル「送信中…」。
**状態** 入力中 / 検証エラー / 送信中（ボタン disable＋spinner で二重送信防止）/ 成功 / 失敗。
**規則** 観測→判断→制御→FB を閉じる——送信結果は同じ文脈で返し、別画面に飛ばさない（03 Cybernetics）。エラーは発生箇所＋原因＋直し方をセットで、責めない（03 Norman）。入力中に責め立てず、blur/送信のタイミングで出す（03 Calm）。
**a11y** `<form>`。送信時は最初のエラー欄へ focus を移し、エラーサマリは `role="alert"`/`aria-live`。各エラーは該当入力に `aria-describedby`＋`aria-invalid`。Enter で送信。
**関連** すべてのフォーム入力 / Button / Alert。

---

### Checkbox  〔—〕

**用途** 独立した二値（オン/オフ）、または複数選択肢から任意個を選ぶ。
**変種** 単独（同意等）／グループ（複数選択）／中間（indeterminate, 親で子の一部選択）。
**構成** ボックス＋チェック/ハイフン記号＋ラベル（クリック可）。
**寸法** ボックス視覚18〜20px＋透明 padding で当たり判定44px以上（10）。ボックス〜ラベル間 spacing-2（8px）、選択肢間 spacing-2 以上。radius 4px（L3）。
**色** 未選択 枠 `--c-line`・地 `--c-surface`。選択 地 `--c-accent`・チェック `--c-on-accent`。disabled 地 `--c-sunk`・記号 `--c-quiet`。error 枠 `--c-danger-border`。
**状態** default / hover（枠 `--c-line-strong`）/ checked / indeterminate / disabled / error。
**規則** 状態はチェック記号（形）で伝え、色だけにしない（10）。即時に効くなら保存ボタン不要、効くまでに保存が要るなら Form に含める。
**a11y** `<input type="checkbox">`＋`<label>`。Space で切替。indeterminate は JS の `.indeterminate` で設定。グループは Fieldset＋legend。
**関連** Radio button / Toggle / Fieldset / Form。

---

### Radio button  〔Radio group〕

**用途** 排他的な選択肢から必ず1つを選ぶ。
**構成** 円＋内側ドット＋ラベル。複数を縦に並べてグループ化。
**寸法** 円 視覚18〜20px＋当たり判定44px、円〜ラベル間 spacing-2（8px）、項目間 spacing-2〜3。
**色** 未選択 枠 `--c-line`。選択 枠/ドット `--c-accent`（地は surface のまま）。disabled `--c-quiet`/`--c-sunk`。
**状態** default / hover / selected / disabled / error。
**規則** 3〜5個程度まではラジオ、それ以上は Select に切替える（一覧走査のコスト, 03 Raskin）。既定値があるなら1つを初期選択。選択は形（ドット）でも判別できること（10）。
**a11y** 同一 `name` の `<input type="radio">` 群、`<fieldset><legend>` でグループ名を与える。矢印キーでグループ内移動、Tab はグループ単位。
**関連** Checkbox / Select / Segmented control / Fieldset。

---

### Toggle  〔Switch〕

**用途** 即時に効く2状態（オン/オフ）の切替。保存ボタンが不要な設定に使う。
**構成** トラック＋つまみ（knob）＋（状態テキスト/左右ラベル）。
**寸法** トラック 幅約44×高さ約24、つまみは内側。当たり判定44px以上。radius は全円（pill）。
**色** オフ トラック `--c-sunk`。オン トラック `--c-accent`・つまみ `--c-on-accent`。disabled `--c-sunk`＋`--c-quiet`。
**状態** off / on / hover / disabled / 反映中（楽観更新し失敗時はロールバック）。
**規則** 即時反映が前提——適用に確認や保存ボタンが要る設定には Toggle でなく Checkbox＋保存を使う（03 Norman: mapping）。状態はつまみ位置＋ラベルで示し色だけにしない（10）。平常は静かに、変化のみ強調（03 Calm）。
**a11y** `role="switch"`＋`aria-checked`（またはネイティブ checkbox）。Space で切替、ラベルと紐付け。on/off を語でも提供する。
**関連** Checkbox / Form / Segmented control。

---

### Select  〔Dropdown〕

**用途** 一覧から1値を選ぶフォーム入力。選択肢が多くラジオでは冗長なとき。
**変種** ネイティブ `<select>`／カスタム listbox（検索や複雑な項目表示が要るとき）。
**構成** トリガー（現在値＋▼）＋オプションリスト（ポップアップ）。
**寸法** トリガー padding `8px 16px`、radius 6px、高さ最小44px。リスト各項目も最小44px。
**色** トリガー 枠 `--c-line`・文字 `--c-ink`、未選択時の placeholder `--c-quiet`。リスト 地 `--c-surface`、hover 項目 `--c-sunk`、選択中 地 `--c-accent-sunk`＋文字 `--c-accent`。
**状態** default / hover / open / focus / disabled / error。
**規則** 可能な限りネイティブ `<select>`（実装が軽く a11y が堅い, 07/10）。▼で開けると示す（signifier）。選択肢が多すぎるなら Combobox で絞れるようにする（03 Raskin）。値選択であり操作起動ではない点で Dropdown menu（actions）と区別する。
**a11y** ネイティブが第一選択。カスタムは `role="listbox"`/`option`、矢印キー移動・Enter 確定・Esc で閉じ、`aria-expanded` を反映。`<label>` 紐付け。
**関連** Combobox / Radio group / Dropdown menu（actions）。

---

### Combobox  〔Autocomplete〕

**用途** 自由入力で候補を絞り込みつつ1値を選ぶ（select＋テキスト入力）。
**構成** テキスト入力＋▼／候補リスト（入力に応じて絞り込み）＋（クリア）。
**寸法** Text input と同じ（padding `8px 16px`、radius 6px、高さ44px）。候補項目は最小44px。
**色** Text input/Select に準拠。一致部分のハイライトは地 `--c-accent-sunk`（または太字）。
**状態** default / focus / 入力中（候補更新）/ 候補なし（空状態文言）/ loading（非同期取得時 spinner）/ disabled / error。
**規則** 候補は入力の文脈で同じ場所に返す（03 Cybernetics）。「該当なし」は空状態で次の手を示す（08）。非同期取得は読込を明示し偽装しない（07 状態可視化）。自由入力を許すか候補限定かを事前に明確化する（03 Norman: 制約の事前提示）。
**a11y** `role="combobox"`＋`aria-expanded`/`aria-autocomplete`/`aria-controls`、現在候補は `aria-activedescendant` で指す。矢印で移動・Enter 確定・Esc で閉じ、`aria-live` で候補件数を通知。`<label>` 紐付け。
**関連** Select / Search input / Text input。

---

### Search input  〔Search〕

**用途** 検索語を入力する。クリア手段と（必要なら）候補を備える。
**構成** 検索アイコン＋入力＋クリア（×）ボタン＋（送信/候補）。
**寸法** padding `8px 16px`（左にアイコン分の余白を確保）、radius 6px、高さ44px。アイコンと×ボタンの当たり判定もそれぞれ確保。
**色** 枠 `--c-line`、アイコン `--c-quiet`、入力 `--c-ink`、placeholder `--c-quiet`。
**状態** 空 / 入力中（×表示）/ 候補表示 / 結果0件（空状態）/ loading。
**規則** 入力があるときだけ×を出し、ワンタップで全消去できる（03 Raskin: アクセスコスト）。placeholder は検索対象の例を示す（「名前・メールで検索」, Norman）が、ラベルの代替にしない。0件は責めず次の手を示す（08）。
**a11y** `<input type="search">` または `role="searchbox"`、`<label>`/`aria-label`。×ボタンは `aria-label="検索語を消去"`。候補があれば Combobox パターンに準拠。
**関連** Combobox / Text input / Empty state（feedback）。

---

### Slider  〔Range〕

**用途** 範囲内の連続値（音量・価格帯等）をつまみで選ぶ。絶対精度より相対調整が要るとき。
**変種** 単一つまみ／二点（範囲指定）。
**構成** トラック＋フィル（選択範囲）＋つまみ＋（現在値ラベル/目盛）。
**寸法** つまみ当たり判定44px、トラック太さ4〜6px、radius は全円。値ラベルはつまみ近傍に置く。
**色** トラック `--c-sunk`、フィル `--c-accent`、つまみ 地 `--c-surface`＋枠 `--c-line-strong`。disabled は彩度を上げず `--c-quiet` 系。
**状態** default / hover / dragging / focus / disabled。
**規則** 現在値を数値でも常時表示する（観測の担保, 03 Cybernetics／判断材料の下限 `M-JUDGMENT-MATERIAL`）。精密な値が要るなら Stepper/数値入力を併設。動きは操作追従のみで装飾アニメは置かない（09）。
**a11y** `<input type="range">` または `role="slider"`＋`aria-valuemin/max/now`/`aria-valuetext`。矢印キーで増減、Home/End で端へ。`<label>` 紐付け。
**関連** Stepper / Text input（number）/ Form。

---

### Stepper  〔Quantity, Counter〕

**用途** ＋/−ボタンで数値を小刻みに増減する（数量・人数等）。
**構成** −ボタン＋数値（入力可）＋＋ボタン。
**寸法** 各ボタン最小44×44px、間隔8px（10）。数値フィールド radius 6px、両端ボタンと一体化し外側角のみ丸める。
**色** ボタン 枠 `--c-line`・記号 `--c-ink`・hover 地 `--c-sunk`。上限/下限到達ボタンは disabled（`--c-quiet`）。
**状態** default / hover / 最小値（−無効）/ 最大値（＋無効）/ disabled。
**規則** 直接入力も許し±だけに強制しない（大きく変えるとき連打は高コスト, 03 Raskin）。範囲端ではボタンを無効化し、なぜ押せないかを形で示す（Norman）。操作には即時 feedback。
**a11y** ±は `<button>`＋`aria-label="増やす/減らす"`、数値は `<input type="number">`＋`<label>`。キーボードの上下キーでも増減。現在値を `aria-live` で通知（任意）。
**関連** Slider / Text input（number）/ Form。

---

### Date input  〔—〕

**用途** 日付を数字フィールドで直接入力する（生年月日など、既知の1日を打てるとき）。
**構成** ラベル＋（年/月/日セグメント または 1フィールド）＋形式例の補助テキスト。
**寸法** padding `8px 16px`、radius 6px、高さ44px。セグメント間は spacing-1〜2。
**色** Text input に準拠。形式ヒントは `--c-muted`、エラー文字 `--c-danger`・枠 `--c-danger-border`。
**状態** default / focus / 不正な日付（error）/ disabled。
**規則** 形式を例で事前提示する（「2026-06-26」「YYYY-MM-DD」, 03 Norman: 制約の事前提示）。エラーは「不正」でなく直し方を示す。先の予約日など見ながら選ぶ用途には Datepicker を併設。
**a11y** `<input type="date">` が第一選択（OS の入力支援と a11y を継承）。テキスト実装時は形式を `aria-describedby`、エラーを `aria-invalid` で伝える。`<label>` 紐付け。
**関連** Datepicker / Text input / Form。

---

### Datepicker  〔Calendar〕

**用途** カレンダー UI で日付（や範囲）を選ぶ。先の日付・空き状況を見ながら選ぶとき。
**変種** 単一日／範囲／月・年ジャンプ付き。
**構成** トリガー入力＋ポップアップカレンダー（月送り＋日グリッド＋今日/選択日の表示）。
**寸法** 日セルは当たり判定最小44px、詰めすぎない間隔。ポップアップ radius 10〜16px（L1〜0）で内部より大きく保つ。
**色** 地 `--c-surface`／枠 `--c-line`。今日 枠 `--c-accent`、選択日 地 `--c-accent`＋文字 `--c-on-accent`、範囲内 `--c-accent-sunk`、無効日 `--c-quiet`。
**状態** default / hover（セル `--c-sunk`）/ 今日 / 選択 / 範囲 / 無効日（選択不可）/ disabled。
**規則** 近い既知の日付は打つほうが速いため Date input を併用する（遠い日はカレンダー、近い既知日は直接入力, 03 Raskin）。選択日は色＋枠/位置でも示す（10）。
**a11y** グリッドは `role="grid"`、日は `gridcell`。矢印キーで日移動・PageUp/Down で月送り・Esc で閉じる。各日に `aria-label`（曜日を含む完全な日付）。トリガーに `aria-haspopup`。
**関連** Date input / Form / Popover（overlays）。

---

### Color picker  〔—〕

**用途** 色を選ぶ（テーマ色・ラベル色など）。
**構成** トリガー（現在色スウォッチ＋値）＋ポップアップ（パレット/スペクトラム＋HEX 入力）。
**寸法** スウォッチ当たり判定最小44px、HEX 入力は Text input 準拠（radius 6px）。プリセット色は spacing-2 間隔。
**色** UI の枠は `--c-line`。選択中スウォッチは `--c-accent` の枠で選択を示す（選択色そのものに頼らない）。
**状態** default / hover / 選択中 / focus / disabled。
**規則** 選択中は枠・チェックなど色以外の手がかりで示す（背景色＝情報なので色だけでは伝わらない, 10）。HEX 等の数値入力も併設し、近似色の判別を支える（判断材料の下限）。
**a11y** 既定は `<input type="color">`。カスタムはスウォッチを `<button>`＋`aria-label`（色名/値）、選択は `aria-pressed`。HEX 入力に `<label>`。コントラスト警告を出せるとなお良い。
**関連** Text input / Popover（overlays）/ Form。

---

### File upload  〔Dropzone〕

**用途** ファイルをアップロードする。クリック選択とドラッグ&ドロップ、進捗・エラーを示す。
**構成** ドロップ領域（アイコン＋説明＋選択ボタン）＋選択済みリスト（名前・サイズ・進捗・削除）。
**寸法** ドロップ領域 padding はバナー基準 `32px 48px`（1:1.5）程度、radius 10px（L1）。各ファイル行は44px、削除ボタンも44px。
**色** 枠は破線 `--c-line-strong`、drag-over 時 枠 `--c-accent`＋地 `--c-accent-sunk`。進捗バー `--c-accent`、成功 `--c-success`、失敗 `--c-danger`＋地 `--c-danger-bg`。
**状態** 空（待機）/ drag-over / アップロード中（進捗%）/ 成功 / 失敗（再試行導線）/ disabled。
**規則** ドロップだけに頼らずクリック選択ボタンを必ず置く（ドロップはキーボード不可, 10）。進捗を実値で示し偽の演出をしない（07 誠実: 見た目＝実装）。失敗は原因（容量超過・形式不可）＋再試行を出す（03 Norman）。許可形式・上限を事前提示。
**a11y** 実体は `<input type="file">`、`<label>`/ボタンで起動。ドロップ領域にはキーボード代替（ボタン）必須。進捗・完了・失敗を `aria-live` で通知。各ファイルの削除に `aria-label`。
**関連** File（display）/ Progress bar（feedback）/ Form。

---

### Rating  〔—〕

**用途** 星などで評価を表示、または設定する。
**変種** 表示専用（読取り）／入力（設定可）／半星対応。
**構成** アイコン（星）列＋（数値/件数ラベル）。
**寸法** 入力時は各星の当たり判定最小44px・間隔8px。表示専用は小さくてよいが数値を併記する。
**色** 満たし `--c-warning`（金色寄り）または `--c-accent`、空 `--c-line-strong`。hover/選択プレビューは満たし色。
**状態** 表示（固定）/ hover（プレビュー）/ selected / disabled。
**規則** 星だけでなく数値（「4.2／5」「件数」）を併記し、形・数でも伝える（10 色非依存／判断材料）。入力時は hover で結果をプレビューする（mapping, 03）。装飾的なアニメは付けない（09）。
**a11y** 入力は radio 群（`role="radiogroup"`／`<input type="radio">`）で実装し、矢印キーで増減、各星に `aria-label`（「5つ星中3つ」）。表示専用は `img`＋`aria-label` か可視数値で伝える。
**関連** Radio group / Badge（feedback）/ Form。

---

### Rich text editor  〔WYSIWYG〕

**用途** 書式付きテキスト（太字・見出し・リスト・リンク等）を編集する。
**構成** ツールバー（書式ボタン群）＋編集領域＋（文字数/保存状態）。
**寸法** ツールバー各ボタン最小44px・間隔8px、関連ボタンは Button group としてまとめる。編集領域 padding `16px 24px`（カード基準）、外枠 radius 10px。
**色** ツールバー 地 `--c-surface`・区切り `--c-line`、適用中ボタンは 地 `--c-accent-sunk`＋文字 `--c-accent`（押下状態を色＋形で）。編集文字 `--c-ink`。
**状態** default / ボタン hover / 書式適用中（active）/ 保存中・保存済（ambient 表示）/ disabled。
**規則** クロームを抑え編集対象を主役にする（07 Deference）。適用中の書式は色だけでなく active 状態（枠/塗り）でも示す（10）。保存状態を常時可視化する（同期中/保存済, 07 / 03 Cybernetics）。曖昧なアイコンにはラベル/ツールチップ（03 Apple Clarity）。頻出書式にショートカット（Raskin）。
**a11y** 編集領域は `role="textbox" aria-multiline="true"`＋`<label>`/`aria-label`。ツールバーは `role="toolbar"`、各ボタンは `aria-pressed`＋ラベル。書式はキーボード（Ctrl+B 等）でも実行可能に。
**関連** Textarea / Button group（actions）/ Tooltip（overlays）。
