cd D:\Data\OpenCV\ObjectDetector\bin
opencv_createsamples.exe
Usage: opencv_createsamples.exe
  [-info  <collection_file_name>]・・・・・・・・・・・ポジティブ画像のリストファイル 
  [-img  <image_file_name>]・・・・・・・・・・・・・・元画像
  [-vec  <vec_file_name>]・・・・・・・・・・・・・・・ベクトル画像ファイル名（*.vec）
  [-bg  <background_file_name>]・・・・・・・・・・・・背景画像のリストファイル
  [-num  <number_of_samples = 1000>] ・・・・・・・・・作成するポジティブ画像の数
  [-bgcolor  <background_color = 0>] ・・・・・・・・・背景色（透過色）
  [-inv] [-randinv]・・・・・・・・・・・・・・・・・・色を反転
  [-bgthresh  <background_color_threshold = 80>] ・・・背景色の許容値（超えた色は透過色）
  [-maxidev  <max_intensity_deviation = 40>] ・・・・・明度差の最大値
  [-maxxangle  <max_x_rotation_angle = 1.100000>]・・・ｘ方向回転角の最大値(rad)
  [-maxyangle  <max_y_rotation_angle = 1.100000>]・・・ｙ方向回転角の最大値(rad)
  [-maxzangle  <max_z_rotation_angle = 0.500000>]・・・ｚ方向回転角の最大値(rad)
  [-show [ <scale = 4.000000>]]・・・・・・・・・・・・変形させたポジティブ画像の確認ウィンドウを表示
  [-w  <sample_width = 24>]・・・・・・・・・・・・・・ベクトル画像の幅
  [-h  <sample_height = 24>] ・・・・・・・・・・・・・ベクトル画像の高さ
opencv_createsamples.exe -img D:\Data\OpenCV\ObjectDetector\Positive\Starfort1.jpg -vec D:\Data\OpenCV\ObjectDetector\Vector\Starfort.vec -num 100 -bgcolor 255 -maxidev 40 -maxxangle 0.8 -maxyangle 0.8 -maxzangle 0.5 -show -w 64 -h 64

cd D:\Data\OpenCV\ObjectDetector\Negative
Get-ChildItem *.jpg -Name > NegativeList.txt
（テキストファイルの書式はANSIでなければならない。画像ファイルにはパスを追加する必要がある。）

cd D:\Data\OpenCV\ObjectDetector\bin
opencv_traincascade.exe
Usage: opencv_traincascade.exe
  -data <cascade_dir_name> ・・・・・・・・・・・・・・・・・・・・・・・分類器の保存先フォルダ（新規には作成されない）
  -vec <vec_file_name> ・・・・・・・・・・・・・・・・・・・・・・・・・ベクトルファイル（*.vec）
  -bg <background_file_name> ・・・・・・・・・・・・・・・・・・・・・・ネガティブ画像のリストファイル
  [-numPos <number_of_positive_samples = 2000>]・・・・・・・・・・・・・ポジティブ画像の枚数（実際のファイル数より少なく設定）
  [-numNeg <number_of_negative_samples = 1000>]・・・・・・・・・・・・・ネガティブ画像の枚数
  [-numStages <number_of_stages = 20>] ・・・・・・・・・・・・・・・・・ステージ数
  [-precalcValBufSize <precalculated_vals_buffer_size_in_Mb = 256>]・・・事前計算した特徴量用バッファサイズ
  [-precalcIdxBufSize <precalculated_idxs_buffer_size_in_Mb = 256>]・・・事前計算したインデックス用バッファサイズ
  [-baseFormatSave]
--cascadeParams--
  [-stageType <BOOST(default)>]
  [-featureType <{HAAR(default), LBP, HOG}>] ・・・・・・・・・・・・・・特徴量のタイプ
  [-w <sampleWidth = 24>]・・・・・・・・・・・・・・・・・・・・・・・・ベクトル画像の幅
  [-h <sampleHeight = 24>] ・・・・・・・・・・・・・・・・・・・・・・・ベクトル画像の高さ
--boostParams--
  [-bt <{DAB, RAB, LB, GAB(default)}>] ・・・・・・・・・・・・・・・・・boost分類器のタイプ
    DAB - Discrete AdaBoost,
    RAB - Real AdaBoost,
    LB - LogitBoost,
    GAB - Gentle AdaBoost.
  [-minHitRate <min_hit_rate = 0.995>] ・・・・・・・・・・・・・・・・・各ステージでの最小ヒット率
  [-maxFalseAlarmRate <max_false_alarm_rate = 0.5>]・・・・・・・・・・・各ステージでの偽判定警告の最大識別率
  [-weightTrimRate <weight_trim_rate = 0.95>]・・・・・・・・・・・・・・トリミング率
  [-maxDepth <max_depth_of_weak_tree = 1>] ・・・・・・・・・・・・・・・弱検出器ツリーの深さ（最大値）
  [-maxWeakCount <max_weak_tree_count = 100>]・・・・・・・・・・・・・・弱検出器ツリー数
--haarFeatureParams--
  [-mode <BASIC(default) | CORE | ALL>]
--lbpFeatureParams--
--HOGFeatureParams--

cd D:\Data\OpenCV\ObjectDetector\bin
opencv_traincascade.exe -data D:\Data\OpenCV\ObjectDetector\cascade\Harr-Like\ -vec D:\Data\OpenCV\ObjectDetector\Vector\Starfort.vec -bg D:\Data\OpenCV\ObjectDetector\Negative\NegativeList.txt -numPos 90 -numNeg 50 -precalcValBufSize 4096 -precalcIdxBufSize 4096 -w 64 -h 64