datadir=$1

pushd $datadir

mkdir exps
echo `date` > exps/log.txt
echo "" >> exps/log.txt

pushd ../TransE
make 
popd

mv ../TransE/Train_TransE exps/
mv ../TransE/Test_TransE exps/

pushd exps

./Train_TransE >> log.txt
echo `date` >> log.txt
echo "" >> log.txt

./Test_TransE bern >> log.txt
echo `date` >> log.txt

popd

popd
