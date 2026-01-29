#  Website Bán Đồ Ăn Vặt

## 1. Giới thiệu đề tài

**Tên đề tài:** Xây dựng website bán đồ ăn vặt sử dụng ngôn ngữ lập trình Python  

**Mục tiêu:**  
Xây dựng một ứng dụng web hoàn chỉnh phục vụ bài toán kinh doanh đồ ăn vặt, có đầy đủ:
- Giao diện người dùng
- Xử lý nghiệp vụ
- Cơ sở dữ liệu
- Phân quyền người dùng
- Thống kê – báo cáo
- Triển khai chạy thực tế

Hệ thống minh họa đầy đủ quy trình nghiệp vụ từ **người dùng truy cập → chọn sản phẩm → đặt hàng → quản lý đơn hàng → thống kê doanh thu**.


## 2. Phạm vi hệ thống

- Website hoạt động theo mô hình Client – Server
- Có tối thiểu **5 thực thể dữ liệu có quan hệ**
- Phục vụ 3 nhóm người dùng: Guest – User – Admin
- Dữ liệu được lưu trữ và quản lý bằng CSDL quan hệ
- Hệ thống có thể mở rộng và phát triển trong tương lai


## 3. Vai trò người dùng

### 3.1 Guest (Khách)
- Xem danh sách sản phẩm
- Tìm kiếm, lọc sản phẩm
- Đăng ký tài khoản
- Đăng nhập hệ thống

### 3.2 User (Người dùng đã đăng nhập)
- Cập nhật thông tin cá nhân
- Thêm sản phẩm vào giỏ hàng
- Đặt đơn hàng
- Xem lịch sử đơn hàng
- Hủy đơn hàng (khi chưa xử lý)

### 3.3 Admin (Quản trị viên)
- Quản lý người dùng
- Quản lý danh mục sản phẩm
- Thêm – sửa – xóa sản phẩm
- Quản lý và duyệt đơn hàng
- Xem thống kê, báo cáo doanh thu


## 4. Các chức năng chính

### 4.1 Xác thực & phân quyền
- Đăng ký tài khoản
- Đăng nhập / đăng xuất
- Phân quyền truy cập theo vai trò (User / Admin)
- Kiểm soát truy cập trang quản trị

### 4.2 Quản lý dữ liệu (CRUD)
- Quản lý **Người dùng**
- Quản lý **Sản phẩm**
- Quản lý **Danh mục**
- Có chức năng tìm kiếm, lọc, sắp xếp

### 4.3 Nghiệp vụ đặc thù
- **Luồng 1:** Đặt hàng  
  Trạng thái: `Pending → Approved → Completed / Canceled`
- **Luồng 2:** Duyệt đơn hàng (Admin)

### 4.4 Thống kê – báo cáo
- Thống kê số lượng đơn hàng theo ngày/tháng
- Thống kê doanh thu theo danh mục sản phẩm

### 4.5 Upload & xử lý tệp
- Upload hình ảnh sản phẩm
- Giới hạn định dạng (jpg, png)
- Giới hạn dung lượng file


## 5. Thiết kế cơ sở dữ liệu (ERD)

### Các thực thể chính
1. **User**
2. **Role**
3. **Category**
4. **Product**
5. **Order**
6. **OrderDetail**

### Quan hệ dữ liệu
- User – Order: 1 – n  
- Category – Product: 1 – n  
- Order – Product: n – n (thông qua OrderDetail)  
- Role – User: 1 – n  


## 6. Kiến trúc & công nghệ sử dụng

- **Ngôn ngữ:** Python 3.x  
- **Framework:** Flask  
- **CSDL:** MySQL  
- **Frontend:** HTML, CSS, Bootstrap  
- **Template Engine:** Jinja2  
- **ORM / Data Access:** MySQL Connector 
- **Quản lý mã nguồn:** Git + GitHub  



## 7. Cấu trúc thư mục dự án
```
FoodShop/
├── foodshop/
│   ├── instance/
│   │   └── shop.db              # Cơ sở dữ liệu SQLite
│   │
│   ├── static/
│   │   └── images/              # Thư mục chứa hình ảnh sản phẩm
│   │       ├── banhca.jpg
│   │       ├── banhtrang.jpg
│   │       ├── khoaitay.jpg
│   │       ├── trasua.jpg
│   │       └── xucxich.jpg
│   │
│   ├── templates/               # Các file giao diện HTML 
│   │   ├── admin.html
│   │   ├── cart.html
│   │   ├── checkout.html
│   │   ├── edit_user.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── orders.html
│   │   ├── register.html
│   │   └── user.html
│   │
│   ├── app.py                   # File chính chạy Flask
│   ├── databasedb.py            # Xử lý kết nối & thao tác CSDL
│   └── shop.db                  # Database 
│
└── README.md                    # Tài liệu mô tả dự án

```
## 8. Dữ liệu mẫu (Seed Data)


- Tài khoản User
  - Username: `dung123@gmail.com`
  - Password: `123456`

  -Username: `vinh690123@gmail.com`
  -Password: `123456`
- Sản phẩm mẫu: Bánh tráng trộn, Bánh cá, Khoai Tây Chiên, Trà Sữa Trân Châu, Snack Rong Biển


