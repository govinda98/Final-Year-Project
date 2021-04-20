mkdir $HOME/bazel-3.4.1
cd $HOME/bazel-3.4.1
wget https://github.com/bazelbuild/bazel/releases/download/3.4.1/bazel-3.4.1-dist.zip
sudo apt-get install build-essential openjdk-8-jdk python zip unzip
unzip bazel-3.4.1-dist.zip
//check error log
pip install protobuf
env EXTRA_BAZEL_ARGS="--host_javabase=@local_jdk//:jdk" bash ./compile.sh
sudo cp output/bazel /usr/local/bin/
cd..
git clone https://github.com/google/mediapipe.git
cd mediapipe
sudo apt-get install libopencv-core-dev libopencv-highgui-dev
sudo apt-get install libopencv-calib3d-dev libopencv-features2d-dev
sudo apt-get install libopencv-imgproc-dev libopencv-video-dev
