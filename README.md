# aixff.org

**2026 AI国际影展 · AI International Film Festival** 官方网站

- 域名：https://aixff.org （GitHub Pages + Cloudflare）
- 内容数据源：[`src.md`](src.md)（提取自 jianpian.cn 链接）
- 技术栈：纯静态 HTML/CSS/JS，零依赖、零构建，直接部署 GitHub Pages

## 目录结构

```
├── index.html           # 首页（Hero · 关于 · 日程 · 组织 · 会后周边 · 联系）
├── submit.html          # 报名参赛（58 项作品竞赛 · 参赛要求 · 20 项技术奖 · 报名回执）
├── conference.html      # 会议征稿（AIVTA 2026）
├── expo.html            # 展位申请（展览招展 · 参会费用）
├── assets/
│   ├── css/style.css    # 设计系统
│   └── js/main.js       # 语言切换 / 导航
├── CNAME                # GitHub Pages 自定义域名 aixff.org
└── src.md               # 影展信息数据源
```

## 本地预览

```bash
python3 -m http.server 8000
# 打开 http://localhost:8000
```

## 部署

推送到 GitHub main 分支即触发 GitHub Pages（见 Settings → Pages → Deploy from branch: main, / root）。
