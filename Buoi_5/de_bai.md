BTVN Buổi 5
Bài 1:

    Tạo một từ điển gồm có các khóa là Mã sinh viên, các giá trị lưu trữ là Điểm tổng kết của sinh viên.
    - Cho biết có bao nhiêu sinh viên có điểm tổng kết trong đoạn [3.0, 3.5].
    - Bổ sung thêm 1 sinh viên vào từ điển.
    - Xóa mọi sinh viên có điểm tổng kết nhỏ hơn 2.0 ra khỏi từ điển.
    - In toàn bộ từ điển ra màn hình.

Bài 2:

    Cho 1 chuỗi được nhập từ bàn phím. In ra 1 dict có có key là các kí tự trong chuỗi và value là số lần kí tự đó xuất hiện trong chuỗi.

Bài 3:

    Bạn A đang được giao nhiệm vụ là lập N (10 <= N <= 100000) tài khoản sinh viên cho Trường Đại Học Công Nghiệp theo với format như sau:

    - Tên tài khoản chính là Mã Sinh Viên tuần tự là 2023600001,
    2023600002, … (việc tạo mã sinh viên phải đảm bảo độ dài luôn là
    10).
    - Mật khẩu chính là một string được lấy random trong list
    [CNTT; KHMT; KTPM; HTTT] + mã số sinh viên. (Gợi ý: Sử dụng
    hàm choice() trong thư viện random).
    - Yêu Cầu : Em hãy tạo 1 dictionary chứa thông tin tài khoản của N sinh viên với mỗi phần tử trong dictionary lưu dictionary con theo dạng:
    “Account + (vị trí [i] +1)”:{
    “Username”: lưu tên tài khoản tại đây
    “Password”: lưu mật khẩu của tài khoản này tại đây}

    Ví dụ về dictionary con:
    “Account1” : {
    “Username”: 2023600001,
    “Password”: KTPM2023600001    #lưu ý đây là random ra KTPM
    }

Bài 4:

    Tạo một từ điển chứa nội dung file CONFIG sau:
    n           | 1500
    m           | 2
    CLUSTERS    | 3
    ITER        | 10000
    METHOD      | FCM
    MEASURE     | EUCLIDEAN
    YEARS       | 51


    - In nội dung từ điển ra màn hình.
    - Sửa lại thông số MEASURE = “MANHATAN”, in kết quả.
    - Cho biết thông số METHOD hiện đang được đặt là gì (in ra màn hình).
    - Bổ sung thêm thông số “LOSS FUNCTION” có giá trị là “NORM_2”, in kết
    quả.
    - Xóa thông số YEARS trong từ điển, in kết quả.
    - Nhập vào một xâu S từ bàn phím. Cho biết S có trùng với giá trị của thông số
    nào trong file CONFIG hay không?
    - Tạo một set chứa toàn bộ giá trị của các thông số trong file CONFIG ở trên, in
    kết quả.
    - Tạo một list chứa toàn bộ giá trị của các thông số trong file CONFIG ở trên, in
    kết quả.
