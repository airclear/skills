
# anthropic-diagram

[English](./README.md) | 中文

一个 Claude Code 技能，用于生成具有 [Anthropic 技术博客](https://claude.com/blog/product-management-on-the-ai-exponential) 视觉语言风格的编辑型图表，简洁、温暖，并输出为 `.drawio` 文件。

---

## 输出样例


![agent-loop-event-system](../images/anthropic-diagram/agent-loop-event-system.drawio.png)

## 它的作用

给 Claude 一段对任意流程、系统或概念的描述。这个技能会：

1. 分析请求并识别合适的可视化模式
2. 先写出一个 `DiagramSpec`——在处理 XML 之前制定的结构化方案
3. 生成完整且带样式的 draw.io XML
4. 将其保存为 `.drawio` 文件，并自动打开

**输出格式**：`.drawio` 文件（可在 [draw.io](https://www.drawio.com/) / diagrams.net 中编辑），并可选择导出为 PNG/SVG。

**使用方法**：打开 http://draw.io 网站，在 Create New Diagram 页面，直接将`.drawio` 文件拖入网站即可。

---

## 视觉风格

Anthropic 博客图表风格由几个关键原则定义：

* **温暖的画布** —— 背景色为 `#F2EFE8`，而不是纯白
* **颜色用于传达含义，而非装饰** —— 每种语义角色（用户输入、错误状态、决策等）都有专属的填充色 / 描边色组合
* **开放式 V 形箭头** —— 这是最具辨识度的元素；绝不使用实心三角箭头
* **带柔和圆角的正交连接线** —— 干净、规整，绝不使用对角线
* **外边框框架** —— 每张图都包裹在一个细线条的圆角矩形中，呈现出很好般的完成感
* **大型编辑风格标题** —— 加粗、深色、水平居中
* **无阴影、无渐变、无高饱和色彩** —— 对比克制，层级主要依靠字体排版与留白来呈现

下面是这段内容的中文翻译：

## 图表模式

该技能会根据图表需要表达的论点，从 12 种模式中选择最合适的一种：

| 模式                                               | 适用场景             |
| ------------------------------------------------ | ---------------- |
| **线性工作流（Linear Workflow）**                       | 顺序步骤，一个环节引出下一个环节 |
| **反馈循环工作流（Feedback Loop Workflow）**              | 重试、迭代、评估闭环       |
| **分支工作流 / 决策树（Branch Workflow / Decision Tree）** | 分支逻辑、路由、审批关卡     |
| **并行发散 / 汇聚（Parallel Fan-out / Fan-in）**         | 并发执行者、结果聚合       |
| **分屏对比（Split Comparison）**                       | 前后对比、两种方案并排展示    |
| **分组式架构（Grouped Architecture）**                  | 系统边界、组件、包含关系     |
| **分层堆栈（Layered Stack）**                          | 层级关系、抽象层、依赖关系    |
| **泳道时序图（Swimlane Sequence）**                     | 多个参与者随时间发生交互     |
| **中心辐射（Hub-and-Spoke）**                          | 一个核心概念及其支撑性想法    |
| **维恩 / 重叠（Venn / Overlap）**                      | 共享归属、领域汇合        |
| **编辑型图表（Editorial Chart）**                       | 数值比较、指标对照        |
| **注释标注（Callout Annotation）**                     | 用于解释主图的补充说明      |

这些模式可以组合使用（例如“分组式架构 + 注释标注”），但始终必须有一个主模式。

---

## 语义化颜色系统

颜色的分配依据是**语义角色**，而不是审美装饰。这种映射在所有图表中都保持一致：

| 角色                   | 填充色       | 描边色       |
| -------------------- | --------- | --------- |
| 主要 / 中性              | #E6E2DA | #8C867F |
| 次要 / 上下文（文件、工具、文档）   | #EAF4FB | #6FA8D6 |
| 第三层 / 控制（路由、记忆、编排）   | #EEEAF9 | #9A90D6 |
| 起始 / 触发（用户输入、外部触发）   | #F8E9E1 | #D88966 |
| 结束 / 成功              | #CFE8D7 | #71AE88 |
| 警告 / 重置（重试、中断）       | #F3E4DA | #C88E6A |
| 决策（分支、关卡、审批）         | #E6D7B4 | #BFA777 |
| AI / LLM（模型调用、代理工作者） | #D7E6DC | #7FB08F |
| 非活动 / 已禁用            | #EFECE6 | #B4AEA6 |
| 错误                   | #F8DFDA | #D96B63 |

这意味着读者无需先阅读标签，仅凭颜色就能一眼判断结构角色。


## 如何安装

该技能是为 Claude Code 设计的。安装方法如下：

1. 将 `skill.md` 文件和 `references/` 目录复制到你的 Claude Code skills 文件夹中（通常是 `~/.claude/skills/anthropic-diagram/`，或者项目级目录 `.claude/skills/anthropic-diagram/`）。
2. Claude Code 会自动检测并加载这个技能。

> **前置条件**：如果你希望生成后自动打开文件或者自动生成 PNG 格式，则需要先安装 [draw.io Desktop](https://www.drawio.com/)。

---

## 如何使用

只需要用自然语言描述你想要可视化的内容即可。该技能会在如下请求中自动触发：

* “画一个 agent 循环的示意图”
* “创建一个展示 RAG 检索工作原理的流程图”
* “把上下文工程的前后对比可视化出来”
* “为这个系统制作一张架构图”
* “画一张流程图，展示 agent 的工作原理”

不需要任何特殊语法。该技能同时支持英文和中文——图中的标签会自动匹配你所使用的语言。


### 示例提示词

```text
画一张图，展示 LLM agent 如何使用工具：模型接收用户提示，
判断是否需要调用工具，执行工具，然后利用结果生成回复。
```

```text
创建一张对比图：左侧是一个朴素的 RAG 流水线；
右侧是一个加入重排序和查询扩展的上下文工程版本。
```

```text
画一张架构图，展示 multi-agent 系统中 planner、worker 和 verifier 的关系。
```

### PNG/SVG 导出

生成 `.drawio` 文件后，你可以将其导出：

```bash
# PNG 导出（Windows，已安装 draw.io Desktop）
"C:\Program Files\draw.io\draw.io.exe" -x -f png -e -b 20 -o output.png input.drawio

# SVG 导出
"C:\Program Files\draw.io\draw.io.exe" -x -f svg -e -b 20 -o output.svg input.drawio
```

> **前置条件**：需要先安装 [draw.io Desktop](https://www.drawio.com/)。


## 文件结构

```text
anthropic-diagram/
├── skill.md                      # 主技能提示文件（工作流、XML 模板、质量检查清单）
├── references/
│   ├── color-palette.md          # 所有颜色、字体、几何参数的唯一事实来源
│   └── pattern-library.md        # 12 种图表模式，包含布局规则与反模式
└── README.md                     # 本文件
```

**`skill.md`** —— 技能的入口文件。定义了五步工作流、所有 XML 样式字符串、布局规则，以及生成前的质量检查清单。

**`references/color-palette.md`** —— 品牌风格参考文件。包含全部颜色标记、语义映射规则、容器规范、连接线规范和字体层级。若要在不改动工作流逻辑的前提下，将该技能适配为另一种视觉风格，可编辑此文件。

**`references/pattern-library.md`** —— 结构参考文件。定义了每种模式的适用场景、对应的布局规则、应避免的反模式，以及模式组合规则。同时也包含密度指南（简单 / 中等 / 密集）和视觉审查清单。

---

## 设计理念

> 一张好的图表不应只是展示信息，而应让其所表达的观点一目了然。

这个技能建立在三个理念之上：

1. **先模式，后像素** —— 先选择正确的结构模式，再处理样式
2. **语义化颜色** —— 每一种颜色选择都在传达含义，因此颜色本身就是信息
3. **克制是一种质量信号** —— 不用阴影、不用渐变、不过度装饰；平静、留白的风格比繁杂的设计更显可信

这些原则正是“编辑型技术图表”（用于在文章中解释观点）区别于 UI 仪表盘或企业架构工具图的关键所在。

---

## 许可证

MIT