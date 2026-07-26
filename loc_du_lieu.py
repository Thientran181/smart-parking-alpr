import os

ID_O_TO = '0'
thu_muc_nhan_goc = './dataset/labels'

for thu_muc_hien_tai, danh_sach_thu_muc_con, danh_sach_file in os.walk(thu_muc_nhan_goc):
    for ten_file in danh_sach_file:
        if ten_file.endswith('.txt'):
            duong_dan_file_txt = os.path.join(thu_muc_hien_tai, ten_file)

            with open(duong_dan_file_txt, 'r') as f:
                cac_dong = f.readlines()

            cac_dong_giu_lai = []
            for dong in cac_dong:
                if not dong.startswith(f"{ID_O_TO} "):
                    cac_dong_giu_lai.append(dong)

            if len(cac_dong_giu_lai) == 0:
                os.remove(duong_dan_file_txt)

                duong_dan_anh = duong_dan_file_txt.replace('labels', 'images').replace('.txt', '.png')

                if os.path.exists(duong_dan_anh):
                    os.remove(duong_dan_anh)
            else:
                with open(duong_dan_file_txt, 'w') as f:
                    f.writelines(cac_dong_giu_lai)

print("Đã dọn dẹp xong toàn bộ dữ liệu ở mọi thư mục con!")