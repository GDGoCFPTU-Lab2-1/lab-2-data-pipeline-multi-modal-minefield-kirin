# BÁO CÁO KẾT QUẢ LAB: THE MULTI-MODAL MINEFIELD

**Họ và tên:** Nguyễn Hữu Huy  
**MSSV:** 2A202600166  
**Ngày thực hiện:** 24/04/2026\
Email: huyhuu0107@gmail.com  
github-username: kirin017   
---

## 1. Mục tiêu
Xây dựng một hệ thống Data Pipeline mạnh mẽ để thu nạp và xử lý dữ liệu từ nhiều nguồn khác nhau (PDF, CSV, HTML, Transcript, Python Code), đảm bảo tính toàn vẹn và chất lượng dữ liệu cho một Cơ sở tri thức (Knowledge Base).

## 2. Các công việc đã thực hiện

### 2.1. Thiết lập môi trường & Schema
- Khởi tạo môi trường ảo Python và cài đặt các phụ thuộc (`pandas`, `beautifulsoup4`, `google-generativeai`, `pydantic`).
- Định nghĩa schema `UnifiedDocument` thống nhất cho mọi nguồn dữ liệu, hỗ trợ lưu trữ metadata đặc thù cho từng loại file.

### 2.2. Xử lý dữ liệu đa nguồn (ETL/ELT)
- **PDF (Gemini API):** Sử dụng mô hình `gemini-3-flash-preview` để phân tích file PDF phức tạp, trích xuất Tiêu đề, Tác giả và tóm tắt nội dung.
- **CSV:** Xử lý dữ liệu bán hàng, làm sạch các trường giá trị "nhiễu" ($1200, "five dollars", "N/A"), chuẩn hóa định dạng ngày tháng và loại bỏ các bản ghi trùng lặp ID.
- **HTML:** Bóc tách dữ liệu từ bảng danh mục sản phẩm, loại bỏ các thành phần giao diện (boilerplate) để lấy thông tin sản phẩm sạch.
- **Transcript (Video):** Loại bỏ các thẻ nhiễu (`[Music]`, `[inaudible]`) và trích xuất thành công giá trị số từ chữ viết tiếng Việt ("năm trăm nghìn").
- **Legacy Code:** Sử dụng thư viện `ast` để đọc docstring của hàm và regex để trích xuất các quy tắc nghiệp vụ từ comment mà không cần thực thi code.

### 2.3. Kiểm soát chất lượng & Điều phối (QA & DevOps)
- Triển khai **Quality Gate** để từ chối các tài liệu không đạt chuẩn (nội dung quá ngắn, chứa chuỗi ký tự lỗi như "Null pointer exception").
- Tự động phát hiện và cảnh báo các sai lệch logic (ví dụ: thuế suất thực tế trong code khác với mô tả trong comment).
- Xây dựng **Orchestrator** để kết nối toàn bộ quy trình và xuất kết quả ra file `processed_knowledge_base.json`.

## 3. Kết quả đánh giá
Hệ thống đã hoàn thành và vượt qua bài kiểm tra của **Forensic Agent**:

| Tiêu chí kiểm tra | Kết quả | Ghi chú |
| :--- | :---: | :--- |
| Tránh trùng lặp ID (CSV) | **PASS** | Đã loại bỏ các bản ghi trùng lặp. |
| Trích xuất giá từ Audio | **PASS** | Nhận diện đúng 500,000 VND từ tiếng Việt. |
| Cổng kiểm soát chất lượng | **PASS** | Loại bỏ thành công dữ liệu "độc hại". |

**Tổng điểm Forensic: 3/3**

---
*Báo cáo được thực hiện bởi Nguyễn Hữu Huy.*
