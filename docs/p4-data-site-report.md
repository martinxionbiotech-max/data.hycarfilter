# Hycarfilter Phase 4 交付报告：data.hycarfilter 产品数据库子站

> 产出日期：2026-10-25 ｜ 作者：数据产品设计师 + 出口滤清器行业编辑（小筑 ✍️）
> 仓库：`data.hycarfilter`（MkDocs · 产品数据库核心）｜ 依据：`docs/hycarfilter-p1-inventory-architecture.md` §2.2 + 主站 `src/data/products.json`

---

## 1. 交付概览

MkDocs Material 数据子站上线，定位「被检索、被机器读、被引用的基础数据支撑」，**内容零营销**，与主站营销文案零重复。canonical 产品数据集迁入本仓作为唯一事实源。

## 2. MkDocs 页数（共 37 内容页 + 1 404）

| 板块 | 页数 | 说明 |
|---|---|---|
| 首页 | 1 | 数据库定位 / 覆盖范围 / 数据说明（无营销文案） |
| SKU 全量索引 | 1 | 22 型号总表：型号/品类/尺寸/效率/滤材/HS Code |
| 品类分页 | 7 | 每品类全部 SKU 规格表 + 品类技术参数定义 |
| SKU 单页 | 22 | 完整字段规范（标识/尺寸/材质/性能/适配/包装/出口） |
| 交叉引用 | 3 | 适配车型映射 / OE 对照框架 / 出口装箱数据 |
| 数据规范 | 3 | 字段 Schema / 命名规则 / 版本更新日志 |
| **合计** | **37** | |

## 3. 生成脚本说明

`scripts/build-db-pages.py`（Python 3，无第三方依赖）读取 `data/products.json`，一次生成全部数据页：

- `docs/products/index.md` — SKU 全量索引
- `docs/products/{slug}.md` ×7 — 品类页（SKU 表 + 品类技术参数定义）
- `docs/products/{model}.md` ×22 — SKU 单页（全字段规范）
- `docs/crossref/vehicle-fitment.md` — 型号↔适配车型（正排 + 倒排索引）
- `docs/crossref/oe-cross-reference.md` — 型号↔OE 对照框架（标注参考性质）
- `docs/crossref/export-packing.md` — 包装/装箱量（权威）+ 托盘/40HQ（脚本估算）

**估算逻辑**：托盘 1200×1000 mm / 装载高 160 cm；40HQ 有效容积 ≈ 65 m³；外箱尺寸为脚本内每品类假设值（部分型号 override），**不进入权威数据集**——包装/装箱量/净重为权威值，托盘/40HQ 为估算并在页内明确标注假设。

## 4. 一致性机制

1. **唯一事实源**：`data/products.json` 为主站 + 三子站的唯一真值表，任何值只在一处定义。
2. **权威副本同值**：本仓 `data/products.json` 与主站 `src/data/products.json` 字节一致（`diff` 校验 **IDENTICAL**，0 差异）。
3. **零手工抄写**：所有数据页由脚本渲染生成，不手工转录任何数值。
4. **同步流程**（写入 README）：主站改数据 → 复制 `products.json` 入本仓 → `python3 scripts/build-db-pages.py` → `mkdocs build` → 提交推送（`p4-data-*` 标记）。

## 5. build / commit / push

- **build**：`mkdocs build` ✅ 37 内容页（+ 404），1.12s，Material 主题。
- **commit**：`449a9ba` `p4-data: scaffold canonical product database (MkDocs Material)`。
- **push**：origin/main（新分支 `main` 已推送）。
- **同步**：主站与 data 站 `products.json` 0 差异。

## 6. 中文紧凑报告

**MkDocs 页数**：37 内容页 = 首页 1 · SKU 索引 1 · 品类 7 · SKU 单页 22 · 交叉引用 3（适配车型/OE 对照/出口装箱）· 数据规范 3（字段 Schema/命名规则/更新日志）。

**生成脚本**：`scripts/build-db-pages.py` 从 `data/products.json` 一次生成全部数据页（索引/品类/SKU/交叉引用），零手工抄写；托盘/40HQ 为脚本估算并明确标注假设，不污染权威数据。

**一致性机制**：`data/products.json` 为唯一事实源 + 与主站字节一致（diff 0 差异）+ 脚本重建页保证两仓同值；README 写明同步流程（改数据→复制→重建→提交）。

**build**：mkdocs build 37 页全绿。**commit**：`p4-data: scaffold canonical product database`。**push**：origin/main。**同步**：0/0。

**报告路径**：`docs/p4-data-site-report.md`（本文档）。
