sed -i "s/x86_64-linux-gnu/aarch64-linux-gnu/g" third_party/opencv_linux.BUILD **
sudo chmod 755 setup_opencv.sh
pip3 install numPy
export GLOG_logtostderr=1 && bazel run --define MEDIAPIPE_DISABLE_GPU=1 //mediapipe/examples/desktop/hello_world:hello_world