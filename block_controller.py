＃！/ usr / bin / python3
＃-*-コーディング：utf-8-*-

 日時 からインポート 日時
 pprintをインポートする
 コピーをインポート

クラス Block_Controller（オブジェクト）：

    ＃初期化パラメータ
    board_backboard  =  0
    board_data_width  =  0
    board_data_height  =  0
    ShapeNone_index  =  0
    CurrentShape_class  =  0
    NextShape_class  =  0

    ＃GetNextMoveはメイン関数です。
    ＃入力
    ＃nextMove：空のnextMove構造。
    ＃GameStatus：ブロック/フィールド/ジャッジ/デバッグ情報。 
    ＃詳細については、内部のGameStatusデータを参照してください。
    ＃出力
    ＃nextMove：次の形状位置とその他を含むnextMove構造。
    def  GetNextMove（self、nextMove、GameStatus）：

        t1  = 日時。今（）

        ＃GameStatusを印刷する
        印刷（"=============================================== ==> "）
        pprint。pprint（GameStatus、width  =  61、compact  =  True）

        ＃GameStatusからデータを取得する
        ＃現在の形状情報
        CurrentShapeDirectionRange  =  GameStatus [ "block_info" ] [ "currentShape" ] [ "direction_range" ]
        自己。CurrentShape_class  =  GameStatus [ "block_info" ] [ "currentShape" ] [ "class" ]
        ＃次の形状情報
        NextShapeDirectionRange  =  GameStatus [ "block_info" ] [ "nextShape" ] [ "direction_range" ]
        自己。NextShape_class  =  GameStatus [ "block_info" ] [ "nextShape" ] [ "class" ]
        ＃現在のボード情報
        自己。board_backboard  =  GameStatus [ "field_info" ] [ " backboard " ]
        ＃デフォルトのボード定義
        自己。board_data_width  =  GameStatus [ "field_info" ] [ "width" ]
        自己。board_data_height  =  GameStatus [ "field_info" ] [ "height" ]
        自己。ShapeNone_index  =  GameStatus [ "debug_info" ] [ "shape_info" ] [ "shapeNone" ] [ "index" ]

        ＃最適なnextMoveを検索->
        戦略 = なし
        LatestEvalValue  =  - 100000
        ＃現在のブロックShapeで検索
        用 direction0 で CurrentShapeDirectionRange：
            ＃x範囲で検索
            x0Min、x0Max  =  self。getSearchXRange（自己。CurrentShape_class、direction0）
            用 X0 における 範囲（x0Min、x0Max）。
                ＃ドロップダウンブロックのようにボードデータを取得する
                ボード = 自己。getBoard（自己。board_backboard、自己。CurrentShape_class、direction0、X0）

                ＃ボードを評価する
                EvalValue  =  self。calcEvaluationValueSample（ボード）
                ＃ベストムーブを更新
                もし EvalValue  >  LatestEvalValue：
                    戦略 =（direction0、X0、1、1）
                    latestEvalValue  =  EvalValue

                ＃＃＃テスト
                ### NextShapeDirectionRangeのdirection1の場合：
                ### x1Min、x1Max = self.getSearchXRange（self.NextShape_class、direction1）
                ### for x1 in range（x1Min、x1Max）：
                ### board2 = self.getBoard（board、self.NextShape_class、direction1、x1）
                ### EvalValue = self.calcEvaluationValueSample（board2）
                ### EvalValue> LatestEvalValueの場合：
                ###戦略=（direction0、x0、1、1）
                ### LatestEvalValue = EvalValue
        ＃最適なnextMoveを検索<-

        印刷（"===" 、日時。今（）-  T1）
        nextMove [ "strategy" ] [ "direction" ] =  strategy [ 0 ]
        nextMove [ "strategy" ] [ "x" ] =  strategy [ 1 ]
        nextMove [ "strategy" ] [ "y_operation" ] = 戦略[ 2 ]
        nextMove [ "strategy" ] [ "y_moveblocknum" ] = 戦略[ 3 ]
        印刷（nextMove）
        印刷（"######サンプルコード######"）
         nextMoveに戻る

    def  getSearchXRange（self、Shape_class、direction）：
        ＃
        ＃形状方向からx範囲を取得します。
        ＃
        minX、maxX、_、_  =  Shape_class。getBoundingOffsets（direction）＃形状xオフセット[minX、maxX]を相対値として取得します。
        XMIN  =  - 1  * ミンクス
        xMax  =  self。board_data_width  -  maxX
        リターン XMIN、XMAX

    def  getShapeCoordArray（self、Shape_class、direction、x、y）：
        ＃
        ＃指定された形状で座標配列を取得します。
        ＃
        coordArray  =  Shape_class。getCoords（direction、x、y）＃形状の方向x、yから配列を取得します。
        リターン coordArray

    def  getBoard（self、board_backboard、Shape_class、direction、x）：
        ＃ 
        ＃新しいボードを入手します。
        ＃
        ＃バックボードデータをコピーして新しいボードを作成します。
        ＃そうでない場合、元のバックボードデータは後で更新されます。
        ボード = コピー。ディープコピー（board_backboard）
        _board  =  self。ドロップダウン（ボード、Shape_class、方向、x）
        リターン _board

    def  dropDown（self、board、Shape_class、direction、x）：
        ＃ 
        ＃getBoardの内部関数。
        ＃-ボード上の形状をドロップダウンします。
        ＃ 
        dy  =  self。board_data_height  -  1
        coordArray  =  self。getShapeCoordArray（Shape_class、direction、x、0）
        ＃更新dy
        以下のための _x、_y で coordArray：
            _yy  =  0
            一方、 _yy  +  _y  < 自己。board_data_height 及び（_yy  +  _y  <  0 または ボード[（_y  +  _yy）* 自己。board_data_width  +  _x ] == 自己。ShapeNone_index）：
                _yy  + =  1
            _yy-  =  1
             _yy  <  dyの場合：
                dy  =  _yy
        ＃新しいボードを入手
        _board  =  self。dropDownWithDy（board、Shape_class、direction、x、dy）
        リターン _board

    def  dropDownWithDy（self、board、Shape_class、direction、x、dy）：
        ＃
        ＃dropDownの内部関数。
        ＃
        _board  = ボード
        coordArray  =  self。getShapeCoordArray（Shape_class、direction、x、0）
        以下のための _x、_y で coordArray：
            _board [（_y  +  dy）*  self。board_data_width  +  _x ] =  Shape_class。形状
        リターン _board

    def  calcEvaluationValueSample（self、board）：
        ＃
        ＃評価ボードのサンプル関数。
        ＃
        幅 = 自己。board_data_width
        高さ = 自己。board_data_height

        ＃評価パラメータ
        ##削除する行
        fullLines  =  0
        ##ラインの穴またはブロックの数。
        nHoles、nIsolatedBlocks  =  0、0
        ## MaxYの絶対微分値
        absDy  =  0
        ##ブロックの蓄積方法
        BlockMaxY  = [ 0 ] * 幅
        holeCandidates  = [ 0 ] * 幅
        holeConfirm  = [ 0 ] * 幅

        ###チェックボード
        ＃各y行
        用 Y における 範囲（高さ -  1、0、- 1）：
            hasHole  =  False
            hasBlock  =  False
            ＃各x行
            用 X における 範囲（幅）：
                ##穴またはブロックがあるかどうかを確認します。
                 ボードの場合[ y  *  self。board_data_width  +  x ] ==  self。ShapeNone_index：
                    ＃ 穴
                    hasHole  =  True
                    holeCandidates [ x ] + =  1   ＃各列の候補のみ。
                その他：
                    ＃ブロック
                    hasBlock  =  True
                    BlockMaxY [ x ] =  height  -  y                 ＃blockMaxYを更新
                    もし holeCandidates [ X ] >  0：
                        holeConfirm [ x ] + =  holeCandidates [ x ]   ＃ターゲット列の穴の数を更新します。
                        holeCandidates [ x ] =  0                 ＃リセット
                    もし holeConfirm [ X ] >  0：
                        nIsolatedBlocks  + =  1                  ＃分離されたブロックの数を更新

            もし hasBlock  == 真 と hasHole  == 偽：
                ＃ブロックでいっぱい
                fullLines  + =  1
            elif  hasBlock  ==  True および hasHole  ==  True：
                ＃ 何もしない
                パス
            elif  hasBlock  ==  False：
                ＃ブロックラインなし（そしてもちろん穴なし）
                パス

        ＃nHoles
        以下のため のx で holeConfirm：
            nHoles  + =  abs（x）

        ### MaxYの絶対微分値
        BlockMaxDy  = []
        以下のために I に 範囲（lenの（BlockMaxY）-  1）：
            ヴァル =  BlockMaxY [ I ] -  BlockMaxY [ I + 1 ]
            BlockMaxDy  + = [ val ]
        以下のため のx で BlockMaxDy：
            absDy  + =  abs（x）

        #### maxDy
        #maxDy = max（BlockMaxY）-min（BlockMaxY）
        #### maxHeight
        #maxHeight = max（BlockMaxY）-fullLines

        ＃＃ 統計データ
        #### stdY
        #if len（BlockMaxY）<= 0：
        ＃stdY = 0
        ＃そうしないと：
        ＃stdY = math.sqrt（sum（[y ** 2 for y in BlockMaxY]）/ len（BlockMaxY）-（sum（BlockMaxY）/ len（BlockMaxY））** 2）
        #### stdDY
        #if len（BlockMaxDy）<= 0：
        ＃stdDY = 0
        ＃そうしないと：
        ＃stdDY = math.sqrt（sum（[y ** 2 for y in BlockMaxDy]）/ len（BlockMaxDy）-（sum（BlockMaxDy）/ len（BlockMaxDy））** 2）


        ＃計算評価値
        スコア =  0
        スコア = スコア +  fullLines  *  10.0            ＃行を削除しよう
        スコア = スコア -  nHoles  *  1.0                ＃は、make穴しないようにしよう
        スコア = スコア -  nIsolatedBlocks  *  1.0       ＃は、孤立ブロックをしないようにしてみてください
        スコア = スコア -  absDy  *  1.0                スムーズにブロックを置くために＃トライ
        ＃score =スコア-maxDy * 0.3＃maxDy
        ＃score =スコア-maxHeight * 5＃maxHeight
        ＃score =スコア-stdY * 1.0＃統計データ
        ＃score =スコア-stdDY * 0.01＃統計データ

        ＃print（score、fullLines、nHoles、nIsolatedBlocks、maxHeight、stdY、stdDY、absDy、BlockMaxY）
        リターン スコア


BLOCK_CONTROLLER_SAMPLE  =  Block_Controller（）
