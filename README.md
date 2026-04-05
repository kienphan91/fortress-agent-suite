# Fortress Agent Suite

**Fortress** là bộ công cụ tối ưu cho các OpenClaw agent trong môi trường production, cung cấp khả năng tự phục hồi (self-healing), giám sát hệ thống và bảo mật chủ động.

Được đóng góp cho cộng đồng OpenClaw toàn cầu dưới giấy phép MIT.

## Tính năng chính
- 🛡️ **Self-Healing**: Tự động phát hiện gateway down, restore từ backup gần nhất và khởi động lại.
- 🩺 **Health Monitoring**: Giám sát disk/memory, tự động dọn log/rác hệ thống.
- ⚙️ **Automated Maintenance**: Tự động hóa cron jobs, audit bảo mật và đồng bộ workspace (git auto-commit).
- 🤖 **Model Manager**: Tự động quản lý danh sách LLM khả dụng cho 9Router.

## Cài đặt
1. Clone bộ suite này về workspace của bạn: `git clone https://github.com/kien-pn/fortress-agent-suite.git`
2. Cài đặt dependency: `pip install psutil`
3. Cấu hình crontab bằng cách thêm nội dung từ `crontab_template.txt`.

## Đóng góp
Chúng tôi chào đón mọi đóng góp từ cộng đồng. Hãy mở Pull Request nếu bạn có ý tưởng mới để làm các AI Agent trở nên "bất tử".

## License
MIT
