# data.hycarfilter

**Hycarfilter canonical product database** — MkDocs 子站，产品数据唯一事实源（machine-readable）。

定位：被检索、被机器读、被引用的基础数据支撑。纯结构化数据 / 规格 / 交叉引用，**内容零营销**，与主站 `hycarfilter.com` 营销文案零重复。

## 目录结构

```
data.hycarfilter/
├── mkdocs.yml                  # MkDocs Material 配置 + nav
├── requirements.txt            # mkdocs / mkdocs-material
├── data/
│   └── products.json           # ★ 权威数据集（canonical 唯一值表，与主站同值）
├── scripts/
│   └── build-db-pages.py       # ★ 从 JSON 生成全部数据页（零手工抄写）
└── docs/
    ├── index.md                # 首页：定位 / 覆盖范围 / 数据说明
    ├── products/
    │   ├── index.md            # SKU 全量索引（生成）
    │   ├── {slug}.md           # 7 品类分页（生成）
    │   └── {model}.md          # 22 SKU 单页（生成）
    ├── crossref/               # 交叉引用（生成）
    │   ├── vehicle-fitment.md      # 型号 ↔ 适配车辆类型
    │   ├── oe-cross-reference.md   # 型号 ↔ OE 对照（参考性质）
    │   └── export-packing.md       # 包装 / 装箱 / 托盘 / 40HQ 估算
    └── specification/          # 数据规范（手写）
        ├── field-schema.md         # 字段 schema
        ├── naming-rules.md         # 命名规则 hy-{品类码}-{系列}
        └── changelog.md            # 版本与更新日志
```

## 数据一致性机制（核心约束）

1. **唯一事实源**：`data/products.json` 是主站 + 三个子站的唯一真值表。**任何值只在一处定义**。
2. **权威副本同值**：本仓 `data/products.json` 与主站 `src/data/products.json` **字节一致**（复制入本仓，两仓同值）。
3. **零手工抄写**：数据页全部由 `scripts/build-db-pages.py` 渲染生成，不手工转录任何数值。

## 同步流程（主站改数据 → 本仓重建）

```bash
# 1. 主站仓库 hycarfilter 修改 src/data/products.json 后，复制到本仓（保证同值）
cp ../hycarfilter/src/data/products.json data/products.json

# 2. 校验两仓字节一致（可选）
diff data/products.json ../hycarfilter/src/data/products.json && echo IDENTICAL

# 3. 重建全部数据页（SKU 索引 / 品类页 / SKU 单页 / 交叉引用）
python3 scripts/build-db-pages.py

# 4. 本地构建验证
mkdocs build

# 5. 提交推送（p4-data-* 标记）
git add -A && git commit -m "data: rebuild from products.json vX.Y.Z" && git push
```

> 注意：新增/删除 SKU 时，除运行脚本外，还需同步更新 `mkdocs.yml` 的 `nav.SKU Details` 分组与 `docs/specification/naming-rules.md` 的 series 清单。

## 本地运行

```bash
pip install -r requirements.txt
python3 scripts/build-db-pages.py
mkdocs serve          # http://127.0.0.1:8000
mkdocs build          # 静态输出 site/
```
