cd D:\Data\OpenCV\ObjectDetector\bin
opencv_createsamples.exe
Usage: opencv_createsamples.exe
  [-info  <collection_file_name>]�E�E�E�E�E�E�E�E�E�E�E�|�W�e�B�u�摜�̃��X�g�t�@�C�� 
  [-img  <image_file_name>]�E�E�E�E�E�E�E�E�E�E�E�E�E�E���摜
  [-vec  <vec_file_name>]�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�x�N�g���摜�t�@�C�����i*.vec�j
  [-bg  <background_file_name>]�E�E�E�E�E�E�E�E�E�E�E�E�w�i�摜�̃��X�g�t�@�C��
  [-num  <number_of_samples = 1000>] �E�E�E�E�E�E�E�E�E�쐬����|�W�e�B�u�摜�̐�
  [-bgcolor  <background_color = 0>] �E�E�E�E�E�E�E�E�E�w�i�F�i���ߐF�j
  [-inv] [-randinv]�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�F�𔽓]
  [-bgthresh  <background_color_threshold = 80>] �E�E�E�w�i�F�̋��e�l�i�������F�͓��ߐF�j
  [-maxidev  <max_intensity_deviation = 40>] �E�E�E�E�E���x���̍ő�l
  [-maxxangle  <max_x_rotation_angle = 1.100000>]�E�E�E��������]�p�̍ő�l(rad)
  [-maxyangle  <max_y_rotation_angle = 1.100000>]�E�E�E��������]�p�̍ő�l(rad)
  [-maxzangle  <max_z_rotation_angle = 0.500000>]�E�E�E��������]�p�̍ő�l(rad)
  [-show [ <scale = 4.000000>]]�E�E�E�E�E�E�E�E�E�E�E�E�ό`�������|�W�e�B�u�摜�̊m�F�E�B���h�E��\��
  [-w  <sample_width = 24>]�E�E�E�E�E�E�E�E�E�E�E�E�E�E�x�N�g���摜�̕�
  [-h  <sample_height = 24>] �E�E�E�E�E�E�E�E�E�E�E�E�E�x�N�g���摜�̍���
opencv_createsamples.exe -img D:\Data\OpenCV\ObjectDetector\Positive\Starfort1.jpg -vec D:\Data\OpenCV\ObjectDetector\Vector\Starfort.vec -num 100 -bgcolor 255 -maxidev 40 -maxxangle 0.8 -maxyangle 0.8 -maxzangle 0.5 -show -w 64 -h 64

cd D:\Data\OpenCV\ObjectDetector\Negative
Get-ChildItem *.jpg -Name > NegativeList.txt
�i�e�L�X�g�t�@�C���̏�����ANSI�łȂ���΂Ȃ�Ȃ��B�摜�t�@�C���ɂ̓p�X��ǉ�����K�v������B�j

cd D:\Data\OpenCV\ObjectDetector\bin
opencv_traincascade.exe
Usage: opencv_traincascade.exe
  -data <cascade_dir_name> �E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E���ފ�̕ۑ���t�H���_�i�V�K�ɂ͍쐬����Ȃ��j
  -vec <vec_file_name> �E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�x�N�g���t�@�C���i*.vec�j
  -bg <background_file_name> �E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�l�K�e�B�u�摜�̃��X�g�t�@�C��
  [-numPos <number_of_positive_samples = 2000>]�E�E�E�E�E�E�E�E�E�E�E�E�E�|�W�e�B�u�摜�̖����i���ۂ̃t�@�C������菭�Ȃ��ݒ�j
  [-numNeg <number_of_negative_samples = 1000>]�E�E�E�E�E�E�E�E�E�E�E�E�E�l�K�e�B�u�摜�̖���
  [-numStages <number_of_stages = 20>] �E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�X�e�[�W��
  [-precalcValBufSize <precalculated_vals_buffer_size_in_Mb = 256>]�E�E�E���O�v�Z���������ʗp�o�b�t�@�T�C�Y
  [-precalcIdxBufSize <precalculated_idxs_buffer_size_in_Mb = 256>]�E�E�E���O�v�Z�����C���f�b�N�X�p�o�b�t�@�T�C�Y
  [-baseFormatSave]
--cascadeParams--
  [-stageType <BOOST(default)>]
  [-featureType <{HAAR(default), LBP, HOG}>] �E�E�E�E�E�E�E�E�E�E�E�E�E�E�����ʂ̃^�C�v
  [-w <sampleWidth = 24>]�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�x�N�g���摜�̕�
  [-h <sampleHeight = 24>] �E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�x�N�g���摜�̍���
--boostParams--
  [-bt <{DAB, RAB, LB, GAB(default)}>] �E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�Eboost���ފ�̃^�C�v
    DAB - Discrete AdaBoost,
    RAB - Real AdaBoost,
    LB - LogitBoost,
    GAB - Gentle AdaBoost.
  [-minHitRate <min_hit_rate = 0.995>] �E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�e�X�e�[�W�ł̍ŏ��q�b�g��
  [-maxFalseAlarmRate <max_false_alarm_rate = 0.5>]�E�E�E�E�E�E�E�E�E�E�E�e�X�e�[�W�ł̋U����x���̍ő厯�ʗ�
  [-weightTrimRate <weight_trim_rate = 0.95>]�E�E�E�E�E�E�E�E�E�E�E�E�E�E�g���~���O��
  [-maxDepth <max_depth_of_weak_tree = 1>] �E�E�E�E�E�E�E�E�E�E�E�E�E�E�E�㌟�o��c���[�̐[���i�ő�l�j
  [-maxWeakCount <max_weak_tree_count = 100>]�E�E�E�E�E�E�E�E�E�E�E�E�E�E�㌟�o��c���[��
--haarFeatureParams--
  [-mode <BASIC(default) | CORE | ALL>]
--lbpFeatureParams--
--HOGFeatureParams--

cd D:\Data\OpenCV\ObjectDetector\bin
opencv_traincascade.exe -data D:\Data\OpenCV\ObjectDetector\cascade\Harr-Like\ -vec D:\Data\OpenCV\ObjectDetector\Vector\Starfort.vec -bg D:\Data\OpenCV\ObjectDetector\Negative\NegativeList.txt -numPos 90 -numNeg 50 -precalcValBufSize 4096 -precalcIdxBufSize 4096 -w 64 -h 64