********结果呈现包**********
ssc install estout,replace


*导入数据
cd "D:\PhD PSU\My intented papers\paper3-thesis\state files\region files"
// 读入CSV文件
import delimited "D:\PhD PSU\My intented papers\paper3-thesis\state files\region files\farwest.csv", clear

reg taxrevenueratio agrm minm manm tradem tandwm infm fandim rem pstem hsm piepcm mehim unemployrate


// ******************************结果导出***************************
// *esttab m1 m2 m3 using res.xls,ar2 label
// // esttab m1 m2 m3 using nolagpartytimefixed.rtf,ar2 label
//  esttab m1 m2 using taxrevenue.xls,ar2 label