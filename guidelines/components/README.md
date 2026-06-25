# Components — コンポーネント別 実用ガイド

原則（[01](../01-foundations.md)〜[10](../10-accessibility.md)章）を、実際のコンポーネントへ落とした**実用層**。
コンポーネント体系は [The Component Gallery](https://component.gallery/components/) を参照し、各コンポーネントに本ガイドラインの**規則・トークン・状態・a11y**を適用した。原則が「なぜ・どう」なら、ここは「このコンポーネントは具体的にこう作る」。

> コンポーネントはジャンル非依存の部品。A/B（一般/道具レンズ）の区別は**画面・構成レベル**で効く（[README 適用範囲](../README.md#適用範囲--a-一般原則--b-システム道具レンズ)）。部品自体はどのジャンルでも使う。

---

## どのコンポーネントも継承する共通規則（universal）

各仕様では繰り返さない。**すべてのコンポーネントが下記を満たす**前提で読む。

- **signifier**：操作可能な要素は「押せる/入力できる/開ける」と見た目で分かる（[03](../03-interaction-feedback.md) Norman）。
- **focus**：`:focus-visible` で `outline: 2px solid var(--c-accent); outline-offset: 1px`（[10](../10-accessibility.md)）。
- **状態**：`hover` / `active` / `disabled` を持ち、操作には即時フィードバックを返す（03）。
- **色**：[color-system](../values/color-system.md) の役割（`--c-surface`/`--c-line`/`--c-ink`/`--c-muted`/`--c-accent`/semantic）。**影でなくヘアライン**で面を分ける（[07](../07-restraint-form.md) Rams）。
- **寸法**：`../../tokens.json`（4ptグリッド・非対称padding・黄金比radius）。インタラクティブ要素の最小タッチは 44–48px（10）。
- **コントラスト**：本文 4.5:1 / UI 3:1。状態を**色だけで伝えない**（アイコン/ラベル併用）（10）。
- **抑制**：各部位は情報を運ぶ。装飾だけの部位を置かない（07 / Tufte data-ink）。

---

## 各仕様の形

```
### 名称  〔別名〕
用途    … 何をする部品か・いつ使うか
変種    … バリエーション（あれば）
構成    … anatomy（部位）
寸法    … padding / radius / size（tokens）
色      … color-system の役割割当
状態    … default / hover / active / focus / disabled / (error 等)
規則    … 適用する原則（章ID）＋コピー
a11y    … 要素 / キーボード / role・aria / コントラスト
関連    … 関連コンポーネント
```

---

## カタログ（全60・カテゴリ別）

詳細仕様は各カテゴリファイルへ。

### フォーム入力 → [forms.md](./forms.md)
| 部品 | 別名 | 用途 |
|------|------|------|
| Text input | — | 1行テキストを入力する |
| Textarea | Text box | 複数行テキストを入力する |
| Label | Form label | 入力欄のラベル |
| Fieldset | — | 関連する入力欄をまとめる枠 |
| Form | — | 送信のための入力群 |
| Checkbox | — | 複数選択／二値のオン・オフ |
| Radio button | Radio group | 排他的に1つ選ぶ |
| Toggle | Switch | 即時に効く2状態の切替 |
| Select | Dropdown | 一覧から1値を選ぶフォーム入力 |
| Combobox | Autocomplete | 自由入力で絞り込める select |
| Search input | Search | 検索語を入力する |
| Slider | Range | 範囲内の値をつまみで選ぶ |
| Stepper | Quantity, Counter | ＋/− で数値を増減する |
| Date input | — | 日付を数字フィールドで入力 |
| Datepicker | Calendar | カレンダーで日付を選ぶ |
| Color picker | — | 色を選ぶ |
| File upload | Dropzone | ファイルをアップロードする |
| Rating | — | 星などで評価を表示／設定 |
| Rich text editor | WYSIWYG | 書式付きテキストを編集する |

### アクション → [actions.md](./actions.md)
| 部品 | 別名 | 用途 |
|------|------|------|
| Button | — | アクションを起動する |
| Button group | Toolbar | 関連ボタンをまとめる |
| Link | Anchor | 別リソースへ移動する |
| Dropdown menu | Select menu | ボタンから操作/遷移メニューを開く |
| Segmented control | Toggle button group | ビュー/選択肢を切替える |
| Icon | — | 目的を示す図記号（アイコンボタン含む） |
| Skip link | Screenreader skip | キーボードで本文へ飛ぶ |

### オーバーレイ → [overlays.md](./overlays.md)
| 部品 | 別名 | 用途 |
|------|------|------|
| Modal | Dialog | 前面に出て応答を要求する |
| Drawer | Sheet, Flyout | 端からスライドするパネル |
| Popover | — | クリックで要素から開く小パネル（操作可） |
| Tooltip | Toggletip | hover等で補足説明を出す |
| Toast | Snackbar | 前面に一時的に出る通知 |

### フィードバック・状態 → [feedback.md](./feedback.md)
| 部品 | 別名 | 用途 |
|------|------|------|
| Alert | Banner, Callout | 重要な変化を目立つ形で知らせる |
| Badge | Tag, Chip, Label | 状態・属性・メタ情報の小ラベル |
| Progress bar | Progress | 連続的な進捗を帯で示す |
| Progress indicator | Stepper, Steps | 離散ステップの進行を示す |
| Spinner | Loader | 処理中で操作不可を示す |
| Skeleton | Skeleton loader | 読込中の灰色プレースホルダ |
| Empty state | — | 表示データが無いことと次の行動 |

### ナビゲーション → [navigation.md](./navigation.md)
| 部品 | 別名 | 用途 |
|------|------|------|
| Navigation | Nav, Menu | ナビゲーションリンクの容器 |
| Header | — | 全ページ上部の帯（サイト名＋主ナビ） |
| Footer | — | 下部の著作権・法務・関連リンク |
| Breadcrumbs | Breadcrumb trail | 階層内の現在地を示すリンク列 |
| Tabs | Tabbed interface | 複数パネルを切替える |
| Pagination | — | 情報を複数ページに分割し移動する |
| Tree view | — | 入れ子の階層構造を表示する |

### 表示・コンテンツ → [display.md](./display.md)
| 部品 | 別名 | 用途 |
|------|------|------|
| Card | Tile | 単一エンティティの内容を束ねる容器 |
| Table | Data table | 行と列で大量データを表示する |
| List | — | 関連項目をまとめる（ul/ol/dl） |
| Accordion | Disclosure | 見出しで内容を開閉する縦スタック |
| Heading | — | 区切りを導入する見出し |
| Avatar | — | ユーザーの図像表現 |
| Image | Picture | 画像を埋め込む |
| Icon | — | 図記号（→ actions.md と共有） |
| Quote | Blockquote | 引用・プルクオート |
| Separator | Divider | 要素間の区切り線 |
| Stack | — | 子要素に一定の余白を与える容器 |
| Hero | Jumbotron | ページ先頭の大きな帯（※テンプレ骨格に注意, 01） |
| Carousel | Slider | 複数スライドを順に見せる |
| Video | — | 動画を再生する |
| File | Attachment | ファイル（添付・DL）の表現 |
| Visually hidden | Screenreader only | 視覚的に隠し支援技術にのみ伝える |

---

## 使い方

1. 作る部品をカタログで引き、該当カテゴリの詳細仕様を読む。
2. 共通規則（上記 universal）＋個別仕様を適用。値は `../../tokens.json` / `../values/color-system.md`。
3. 画面に組むときは [01 決定順](../01-foundations.md)（題材から構造／テンプレ骨格禁止）に従い、部品を**目的の構造**へ配置する。部品が揃っていても骨格が定番なら「どこかで見た」画面になる。
