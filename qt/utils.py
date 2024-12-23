import os
import sys
def get_usb_drives():
    usb_drives = []
    if os.name == 'nt':  # Windows 系统
        import string
        from ctypes import windll

        drive_bits = windll.kernel32.GetLogicalDrives()
        for letter in string.ascii_uppercase:
            if drive_bits & 1:
                drive = f"{letter}:\\"
                if os.path.exists(drive):
                    # 检查驱动器类型是否为可移动设备
                    if windll.kernel32.GetDriveTypeW(drive) == 2:  # 2 表示驱动器为可移动设备
                        usb_drives.append(drive)
            drive_bits >>= 1
    return usb_drives


def get_resource_path(relative_path):
    # 如果程序正在运行在 PyInstaller 打包后的环境中，使用 _MEIPASS 目录
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


if __name__ == '__main__':
    usb_drives = get_usb_drives()
    print("U盘盘符:", usb_drives)
