# dnst
NCCU宿舍網路設定工具
Dorm Network Setting Tool for NCCU

### 一、 說明
dnst是適用於政治大學宿舍網路之設定工具，旨在能夠在Windows系統下快速設定網卡固定IP、子網路遮罩、預設閘道，以及DNS。

dnst使用Python編寫，並以pyinstaller編譯為執行檔。亦能透過Python執行Source code。

### 二、 適用平台
* Windows 10
> 20H2
>
> 21H1
>
> 21H2
>
> 22H1
>
> 22H2 (最新版本)(已驗證)

* Windows 11
> 21H2
>
> 22H2 (已驗證)
>
> 23H2 (最新版本)

* Windows Server 2019
> 1809 (已驗證)

### 三、 使用說明
##### 步驟一
請先使用政大電算中心提供之「查卡號小工具」確認「連線名稱」以及「mac address(卡號)」。

##### 步驟二
至電算中心註冊宿網，填入步驟一查到的卡號。

##### 步驟三
以系統管理員權限執行dnst.exe或是直接以Python執行dnst.py，輸入剛剛步驟一查到的「連線名稱」，並按下Enter鍵，再依指示輸入學校分配之「註冊的IP」，並按下Enter鍵，再輸入系統顯示的預設閘道IP位置，程式將自動設定完成。

其餘子網路遮罩以及DNS將設定為以下預設值。

子網路遮罩: 255.255.255.0

慣用DNS伺服器: 140.119.1.110

其他DNS伺服器: 140.119.252.12

##### 步驟四
學校系統將於整點進行更新，屆時將可使用宿舍網路。

### 四、 Future outlook
* IP/ Mask/ Gateway/ DNS Server display.
* Advance setting.
