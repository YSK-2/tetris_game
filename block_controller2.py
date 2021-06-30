＃！/ usr / bin / python3
＃-*-コーディング：utf-8-*-
#test
 日時 からインポート 日時
 pprintをインポートする
 ランダムにインポート

クラス Block_Controller（オブジェクト）：

    ＃initパラメータ
    board_backboard  =  0
    board_data_width  =  0
    board_data_height  =  0
    ShapeNone_index  =  0
    CurrentShape_class  =  0
    NextShape_class  =  0

    ＃GetNextMoveはメイン関数です。
    ＃入力
    ＃GameStatus：このデータにはすべてのフィールドステータスが含まれます。 
    ＃詳細については、内部のGameStatusデータを参照してください。
    ＃出力
    ＃nextMove：このデータには、次の形状の位置とその他の位置が含まれます。
    ＃Noneを返す場合は、nextMoveに何もしません。
    def  GetNextMove（self、nextMove、GameStatus）：

        t1  = 日時。今（）

        ＃GameStatusを印刷する
        印刷（"=============================================== ==> "）
        pprint。pprint（GameStatus、width  =  61、compact  =  True）

        ＃最適なnextMoveを検索->
        ＃ランダムサンプル
        nextMove [ "strategy" ] [ "direction" ] =  random。randint（0、4）
        nextMove [ "strategy" ] [ "x" ] =  random。randint（0、9）
        nextMove [ "strategy" ] [ "y_operation" ] =  1
        nextMove [ "strategy" ] [ "y_moveblocknum" ] =  random。randint（1、8）
        ＃最適なnextMoveを検索<-

        ＃nextMoveを返す
        印刷（"===" 、日時。今（）-  T1）
        印刷（nextMove）
         nextMoveに戻る

BLOCK_CONTROLLER  =  Block_Controller（）
