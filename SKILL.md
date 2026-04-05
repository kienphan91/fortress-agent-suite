# Fortress Agent Suite

**Fortress** là bộ công cụ tối ưu cho các OpenClaw agent trong môi trường production, cung cấp khả năng tự phục hồi (self-healing), giám sát hệ thống và bảo mật chủ động.

## Tính năng chính
- 🛡️ **Self-Healing**: Tự động phát hiện gateway down, restore từ backup gần nhất và khởi động lại.
- 🩺 **Health Monitoring**: Giám sát disk/memory, tự động dọn log/rác hệ thống.
- ⚙️ **Automated Maintenance**: Tự động hóa cron jobs, audit bảo mật và đồng bộ workspace.
- 🤖 **Model Manager**: Tự động quản lý danh sách LLM khả dụng cho 9Router.

## Cài đặt
1. Tải bộ suite về workspace của bạn.
2. Cấp quyền thực thi cho các script trong `scripts/self-healing/`.
3. Chạy `crontab -e` và thêm các job từ file `crontab_template.txt`.

## License
MIT - Đóng góp miễn phí cho cộng đồng OpenClaw toàn cầu.
