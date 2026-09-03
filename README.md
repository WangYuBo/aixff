# aixff.org

**2026 AI国际影展 · AI International Film Festival** 官方网站

- 域名：https://aixff.org （GitHub Pages + Cloudflare）
- 内容数据源：[`src.md`](src.md)（提取自 jianpian.cn 链接）
- 技术栈：纯静态 HTML/CSS/JS，零依赖、零构建，直接部署 GitHub Pages

## 目录结构

```
├── index.html           # 首页（Hero · 三类参与入口 · 关于 · 日程 · 组织 · 到访信息）
├── submit.html          # 作品竞赛（58 项作品奖 · 参赛要求 · 20 项技术奖 · 报名投稿）
├── conference.html      # 会议征稿（AIVTA 2026）
├── expo.html            # 展位申请（展览招展 · 参会费用）
├── assets/
│   ├── css/style.css    # 设计系统
│   └── js/main.js       # 语言切换 / 导航
├── CNAME                # GitHub Pages 自定义域名 aixff.org
└── src.md               # 影展信息数据源
```

## 信息架构

- 全局导航只表达四个站点级目的地：首页、作品竞赛、学术会议、产业展览。
- 首页按创作者、研究者、产业伙伴三类身份分流，不再平铺所有业务子栏目。
- 奖项、要求、费用、收款方式归入对应业务页的页内导航。
- 联系方式作为全站工具信息统一放在页脚，不再占用首页正文和全局导航。

## 本地预览

```bash
python3 -m http.server 8000
# 打开 http://localhost:8000
```

## 部署

推送到 GitHub main 分支即触发 GitHub Pages（见 Settings → Pages → Deploy from branch: main, / root）。
