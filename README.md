# UsefulPythonCollection
## 体温フォーム自動化
### Macの場合
Automatorで定期実行
![](../../../../../var/folders/7k/2j7shpkj7b7g_99m9m2flnm80000gn/T/TemporaryItems/NSIRD_screencaptureui_2jrcK6/スクリーンショット 2022-12-31 16.51.26.png)

![](../../../../../var/folders/7k/2j7shpkj7b7g_99m9m2flnm80000gn/T/TemporaryItems/NSIRD_screencaptureui_kNtnD5/スクリーンショット 2022-12-31 16.52.19.png)

「シェルスクリプトを実行」をドラッグ&ドロップし以下のshellを入力

~~~shell
cd
source ~/.zshrc
cd .log_
touch log-`date +%Y%m%d`.txt
/Users/ユーザー名/opt/anaconda3/envs/仮想環境名/bin/python /Users/ユーザー名/UsefulPythonCollection/SendTMPForm.py
 > log-`date +%Y%m%d`.txt
~~~

カレンダーから「新規イベントを追加」し「通知>カスタム」から先ほど作ったAutomatorファイルを選択し、定期的に実行されるようにする

![](../../../../../var/folders/7k/2j7shpkj7b7g_99m9m2flnm80000gn/T/TemporaryItems/NSIRD_screencaptureui_nUEWwx/スクリーンショット 2022-12-31 16.53.34.png)
### 参考
https://qiita.com/nakayumc0278/items/6b49b15fbaf1f52c51ea
https://www.wholenotism.com/blog/2020/04/timeredexecommand.html