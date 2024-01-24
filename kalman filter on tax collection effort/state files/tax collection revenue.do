*********结果呈现包**********
*ssc install estout,replace


*导入数据
cd "D:\PhD PSU\My intented papers\paper3-thesis\state files"
// 读入CSV文件
// import delimited "D:\PhD PSU\My intented papers\paper3-thesis\state files/ULTRAPLUSFINALmate.csv", clear

// 创建临时数据集
tempfile tempdata
save "`tempdata'", replace
use "`tempdata'", clear
// // // 在临时数据集上删除包含（L）、0或者空值的行
// // use "`tempdata'", clear
// // // drop if var1 == "（L）" | var1 == 0 | missing(var1)
// // // drop if var2 == "（L）" | var2 == 0 | missing(var2)
// //
// // // 如果你有多个变量，可以使用循环
//
local vars taxrevenueratio agrm minm manm tandwm infm fandim rem hsm piepcm tradem pstem mehim unemployrate gdppercapita 

foreach var of local vars {
    destring `var', replace force
}




// foreach var of local vars {
//     egen drop_flag = total(`var' == "（L）" | `var' == 0 | missing(`var'))
//     drop if drop_flag>0
// }
//
// // 查看删除缺失值后的临时数据集
// list var1 var2
//
// // 如果需要保存修改后的数据集，可以使用`save`命令
// save "path/to/your/newdata.dta", replace
//
// summarize
*************数据整理和清洗*********************
// replace agr = . if regexs(1) "[^0-9.]" var1, gen(nonnumeric)
// // replace min = . if regexs(1) "[^0-9.]" var1, gen(nonnumeric)
// // replace str = . if regexs(1) "[^0-9.]" var1, gen(nonnumeric)
//
// destring agr min str, replace float

*删除缺失值
// sum agr min man tra tandw inf fandi re pste hs str gdp spi piepc if missing(agr, min, man, tra, tandw, inf, fandi, re, pste, hs, str, gdp, spi, piepc) == 0
//
// drop if missing(agr, min, man, trade, tandw, inf, fandi, re, hs, str, gdp, taxrevenueratio, spi, piepc, stategovernorparty,mehi, unemployrate,granttotaloutlay,federalfunds,trustfunds,constraintratio) | (agr == 0 | min == 0 | man == 0 | trade == 0 | tandw == 0 | inf == 0 | fandi == 0 | re == 0 | pste == 0 | hs == 0 | str == 0 | gdp == 0 | spi == 0 | piepc == 0 |taxrevenueratio == 0)
//
//
// summarize agr min man trade tandw inf fandi re pste hs str gdp taxrevenueratio spi piepc stategovernorparty mehi unemployrate granttotaloutlay federalfunds trustfunds constraintratio

//  加标签方便结果展示
 label var agr "Agriculture"
 label var min "Mining"
 label var man "Manufacturing"
 label var trade "Wholesale trade and Retail trade"
 label var tandw "Transportation and warehousing"
 label var inf "Information"
 label var fandi "Finance and insurance"
 label var re " Real estate and rental and leasing"
 label var unemployrate "unemployment rate"
 label var hs "Health care and social assistance"
 label var str " State tax reveune"
 label var gdp "GDP"
 label var spi "state personal income"
 label var piepc "person income expenditure per capita"
 label var stategovernorparty "State governor partisan"
 label var mehi "Median household income"
 label var granttotaloutlay "Grants from feedral government"

 label var federalfunds "Federal grants to federal funds"
 label var trustfunds "Federal grants to trust funds"
 label var constraintratio "Level of constraint"
 label var taxrevenueratio "tax revenue ratio to GDP"
 label var region "Geo Region"
 
 
// *********************************************按照地区进行OLS回归并且保存结果***********************************
// reg taxrevenueratio agrm minm manm tandwm infm fandim rem hsm piepcm tradem pstem mehim gdppercapita unemployrate if region == "Far West", robust
// estimates store regfarwest
//
// reg taxrevenueratio agrm minm manm tandwm infm fandim rem hsm piepcm tradem pstem mehim gdppercapita unemployrate if region == "Great Lakes", robust
// estimates store reggreatlakes
//
// reg taxrevenueratio agrm minm manm tandwm infm fandim rem hsm piepcm tradem pstem mehim gdppercapita unemployrate if region == "Mideast", robust
// estimates store regmideast
//
// reg taxrevenueratio agrm minm manm tandwm infm fandim rem hsm piepcm tradem pstem mehim gdppercapita unemployrate if region == "New England", robust
// estimates store regengland
//
// reg taxrevenueratio agrm minm manm tandwm infm fandim rem hsm piepcm tradem pstem mehim gdppercapita unemployrate if region == "Plains", robust
// estimates store regplains
//
// reg taxrevenueratio agrm minm manm tandwm infm fandim rem hsm piepcm tradem pstem mehim gdppercapita unemployrate if region == "Rocky Mountain", robust
// estimates store regrockymountain
//
// reg taxrevenueratio agrm minm manm tandwm infm fandim rem hsm piepcm tradem pstem mehim gdppercapita unemployrate if region == "Southeast", robust
// estimates store regsoutheast
//
// reg taxrevenueratio agrm minm manm tandwm infm fandim rem hsm piepcm tradem pstem mehim gdppercapita unemployrate if region == "Southwest", robust
// estimates store regsouthwest
//
// esttab regfarwest reggreatlakes regmideast regnewengland regplains regrockymountain regsoutheast regsouthwest using regionolsss.xls,ar2 label
******************************************************************************************************************


************************************按照地区进行fe回归并且保存结果****************************************************
// xtset geocode
// xtreg taxrevenueratio agrm minm manm tandwm infm fandim rem hsm piepcm tradem pstem mehim gdppercapita unemployrate if region == "Far West", fe robust
// estimates store xtregfarwest
//
// xtreg taxrevenueratio agrm minm manm tandwm infm fandim rem hsm piepcm tradem pstem mehim gdppercapita unemployrate if region == "Great Lakes", fe robust
// estimates store xtreggreatlakes
//
// xtreg taxrevenueratio agrm minm manm tandwm infm fandim rem hsm piepcm tradem pstem mehim gdppercapita unemployrate if region == "Mideast", fe robust
// estimates store xtregmideast
//
// xtreg taxrevenueratio agrm minm manm tandwm infm fandim rem hsm piepcm tradem pstem mehim gdppercapita unemployrate if region == "New England", fe robust
// estimates store xtregnewengland
//
// xtreg taxrevenueratio agrm minm manm tandwm infm fandim rem hsm piepcm tradem pstem mehim gdppercapita unemployrate if region == "Plains", fe robust
// estimates store xtregplains
//
// xtreg taxrevenueratio agrm minm manm tandwm infm fandim rem hsm piepcm tradem pstem mehim gdppercapita unemployrate if region == "Rocky Mountain", fe robust
// estimates store xtregrockymountain
//
// xtreg taxrevenueratio agrm minm manm tandwm infm fandim rem hsm piepcm tradem pstem mehim gdppercapita unemployrate if region == "Southeast", fe robust
// estimates store xtregsoutheast
//
// xtreg taxrevenueratio agrm minm manm tandwm infm fandim rem hsm piepcm tradem pstem mehim gdppercapita unemployrate if region == "Southwest", fe robust
// estimates store xtregsouthwest
//
// esttab xtregfarwest xtreggreatlakes xtregmideast xtregnewengland xtregplains xtregrockymountain xtregsoutheast xtregsouthwest using xtregionolsss.xls,ar2 label


// // 创建一个变量保存回归系数
// gen beta = .
//
// // 按照 id 分组，对每个组进行回归
// by region: reg trr agrr minr manr trader tandwr infr fandir rer pster hsr piepc mehi unemployrate
// sort region
// by region: reg taxrevenueratio agrr minr manr trader tandwr infr fandir rer pster hsr piepcm mehim unemployrate, robust
// // //
// // // // 将回归系数保存到 beta 变量中
// // esttab using "regression_results_region_`region'.csv", replace
// //
// // // // 查看结果
// // // list region beta
//
// // *获取多重共线性的评估
// // sort region
// // by region: reg taxrevenueratio agrm minm manm tradem tandwm infm fandim rem pstem hsm piepcm mehim unemployrate, robust
// //
// // xtset year
// // by region: xtreg taxrevenueratio agrm minm manm tradem tandwm infm fandim rem pstem hsm piepcm mehim unemployrate, robust fe
//
// // estat vif
// // by region: reg trr agrr minr manr tandwr infr fandir rer pster hsr piepc mehi unemployrate
//
// // *具有多重共线性所以删掉几个最高的然后重新回归重新获取多重共线性的评估
// // reg taxrevenueratio agrr minr manr tandwr infr fandir pster hsr piepcm mehim unemployrate
// // estat vif
// *能不能按照地区分别测算VIF？
// // levelsof region, local(regions)
// //
// // foreach r of local regions {
// //     // 选择每个 region 的子集
// //     keep if region == "`r'"
// //
// //     // 执行回归
// //     reg taxrevenueratio agrr minr manr trader tandwr infr fandir rer pster hsr piepcm mehim unemployrate
// //
// //     // 计算 VIF
// //     estat vif
// //
// //     // 恢复数据集
// //     restore, preserve
// // }
//
// //
// // *解决了多重共线以后检查异方差问题
// // reg taxrevenueratio agrr minr manr tandwr infr fandir pster hsr piepcm mehim unemployrate
// // predict residuals, residuals
// // // 异方差检验
// // hettest residuals
// // // rvpplot manr
// // // rvpplot trader
// // // rvpplot tandwr
// // // rvpplot infr
// // // rvpplot fandir
// // // rvpplot rer
// // // rvpplot pster
// // // rvpplot hsr
// // // rvpplot piepc
// // // rvpplot mehi
// // // rvpplot unemployrate
// //
// // *存在异方差问题所以使用robust标准差
// // by region: reg taxrevenueratio agrr minr manr tandwr infr fandir pster hsr piepcm mehim unemployrate, robust
// // //
// // // *但可能存在遗漏变量等问题，所以使用固定效应模型
// // xtset year
// // by region: xtreg taxrevenueratio agrr minr manr tandwr infr fandir pster hsr piepcm mehim unemployrate,fe robust
// // // 两者对比，最终选择by region的fixed effect regrssion 
// sort region
// xtset year
// by region: xtreg taxrevenueratio agrm minm manm tandwm tradem infm hsm fandim pstem hsm piepcm mehim unemployrate,fe robust
// // 两者对比，最终选择by region的fixed effect regrssion 
// // rvpplot manr
// // rvpplot trader
// // rvpplot tandwr
// rvpplot infr
// rvpplot fandir
// rvpplot rer
// rvpplot pster
// rvpplot hsr
// rvpplot piepc
// rvpplot mehi
// rvpplot unemployrate

******************************************hausman test*************************************************
// * 估计一致但有偏的模型（固定效应模型）
// xtreg dependent_var independent_vars, fe
// estimates store fe_model
//
// * 估计无偏但不一致的模型（随机效应模型）
// xtreg dependent_var independent_vars, re
// estimates store re_model
// hausman fe_model re_model


*****************************************************************************************************************




*自相关检验 自相关图 correlogram 或者BG 检验或者DM检验（stata中的默认检验）或者Q检验（BOX-PIERCE，后来发展为ljund-Box Q），或者DW检验（已经基本淘汰，只能检验一阶自相关）

// *画图
// predict residuals, residuals
// ac residuals
**P阶怎么确认具体是多少阶？看样本量大小，stata默认为min(floor(n/2-2),40)


*解决方法：
*异方差和自相关都出现的时候，robust选项不在合适（只处理异方差），可以选择HAC 标准误，最好建议取p=n^1/4来确定p的阶数
*或者准差分法，
*或者GLS 广义最小二乘，但必须知道距估计的值，这往往是不知道的，所以替代是FGLS，feasible GLS(所以FGLS用的不多))
*修改模型设定（有的自相关是因为模型设定问题，比如动态模型设定为静态模型）
*

// xtline varname





// // 固定效应模型
// xtset year
// eststo m2: by region: xtreg taxrevenueratio agrr minr manr tandwr infr fandir pster hsr piepc mehi unemployrate,fe robust
// estimates store fe_results
// estout fe_results using "fixed_effect_results.csv", replace
// //
// estimates store myreg
// *检查异方差性
// rvpplot manr ci(last)
// *删掉数据中的L和D值
// local str_vars agr min man tra tandw inf fandi re pste hs str gdp spi piepc
//
// foreach str_var of local str_vars {
//     drop if strpos(`str_var', "(L)") > 0 | strpos(`str_var', "(D)") > 0
// }

// replace agr = . if regexs(1) "[^0-9.]" var1, gen(nonnumeric)
//
// destring agr min str, replace float


//
// ******************************结果导出***************************
// *esttab m1 m2 m3 using res.xls,ar2 label
// // esttab m1 m2 m3 using nolagpartytimefixed.rtf,ar2 label
//  esttab m1 m2 using taxrevenue.xls,ar2 label