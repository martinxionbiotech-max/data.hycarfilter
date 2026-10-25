# Hycarfilter Data

**Canonical product database** for hycarfilter — 河北红影汽车配件 · Hebei Hongying Automotive Parts Co., Ltd. (since 2013, Qinghe County, Xingtai, Hebei).

> 定位：被检索、被机器读、被引用的**基础数据支撑**。本子站只承载**结构化数据 / 规格 / 交叉引用**，内容零营销。营销文案与采购决策内容在主站 `hycarfilter.com`，本子站仅被其引用、不与其重复。

## 覆盖范围

| 维度 | 值 |
|---|---|
| 品类 | **7**（空气滤 / 空调滤 / 机油滤 / 燃油滤 / 雨刮 / 变速箱滤网 / LED 车灯） |
| SKU | **22**（seed 数据集，逐品类 2–4 个代表型号） |
| 数据版本 | `0.1.0`（`data/products.json` `_meta.version`） |
| 命名规则 | `hy-{category_code}-{series}`（如 `hy-af-nano`） |
| 字段覆盖 | 标识 / 尺寸 / 材质 / 性能 / 适配 / OE 对照 / 包装 / 出口（MOQ·交期·认证·目标市场·HS Code） |

## 数据说明

1. **唯一事实源（canonical）**：所有型号/参数/规格的**唯一真值**存于本仓 `data/products.json`。主站与 tech/market 子站引用同一文件，**同值跨站唯一**——任何值只在一处定义。
2. **零手工抄写**：本子站所有数据页（SKU 索引、品类页、SKU 单页、交叉引用表）均由 `scripts/build-db-pages.py` 从 JSON 渲染生成，不手工转录任何数值。
3. **参考性质标注**：OE 对照号与竞品件号当前为 `status: seed` 占位/示意值，**未经验证**，交叉引用页已明确标注参考性质。
4. **估算值标注**：托盘/40HQ 装箱量为脚本**估算**，外箱尺寸为脚本内每品类假设值，**不进入权威数据集**；包装/装箱量/净重为权威值。
5. **数据成熟度**：`status` 字段标记 `seed | draft | final`，当前全量 `seed`，随 Phase 4+ 逐步补全核对。

## 快速入口

- [SKU 全量索引](products/index.md) — 22 型号总表（型号/品类/尺寸/效率/滤材/HS Code）
- [品类分页](products/air-filter.md) — 7 品类规格表 + 品类技术参数定义
- [适配车型映射](crossref/vehicle-fitment.md) — 型号 ↔ 适配车辆类型（正/倒排）
- [OE 对照框架](crossref/oe-cross-reference.md) — 型号 ↔ OE 号（参考性质）
- [出口装箱数据](crossref/export-packing.md) — 包装/装箱量/托盘/40HQ 估算
- [字段 Schema](specification/field-schema.md) · [命名规则](specification/naming-rules.md) · [版本与更新日志](specification/changelog.md)
