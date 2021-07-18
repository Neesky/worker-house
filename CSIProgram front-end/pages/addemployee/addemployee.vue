<template>
	<view>
		<view>
			<u-toast ref="uToast" />
		</view>
		
		<!-- 添加员工表单填写信息，其中ID，密码，部门，职位，名字，性别为必填 -->
		<u-form style="margin-left:10px;" :model="form" ref="uForm" >
			<u-form-item :required="true" label="ID"><u-input class="input" v-model="form.id"/></u-form-item>
			
			<!-- 添加员工初始密码设置有格式限制 -->
			<u-form-item :required="true" label="密码">
				<u-input class="input" v-model="form.password" placeholder="密码长度为8-20个字符，必须包含字母和数字" @blur="limit"/>
			</u-form-item>
			
			<!-- 部门名字和职位名字采用下拉框，从后端获取所有名称 -->
			<u-form-item :required="true" label-width=120rpx label="部门名称">
				<u-input class="input1 input2" v-model="form.departmentName" type="select" border="border" @click="showbranch = true"/>
				<u-action-sheet :list="actionSheetListbranch" v-model="showbranch" @click="actionSheetCallbackbranch"></u-action-sheet>
			</u-form-item>
			
			<!-- 部门信息通过部门名称自动从后端获取，不需填写，职位信息同-->
			<u-form-item label="部门信息" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<textarea :value="form.departmentRemark" style="color: #BBBBBB;font-size: 14px;" :disabled=true
						:auto-height=true></textarea>
				</view>
			</u-form-item>
			
			<u-form-item :required="true" label-width=120rpx label="职位名称">
				<u-input class="input1 input2" v-model="form.jobName" type="select" border="border" @click="showpos = true"/></u-form-item>
				<u-action-sheet :list="actionSheetListpos" v-model="showpos" @click="actionSheetCallbackpos"></u-action-sheet>
			</u-form-item>
			
			<u-form-item label="职位信息" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<textarea :value="form.jobRemark" style="color: #BBBBBB;font-size: 14px;" :disabled=true
						:auto-height=true></textarea>
				</view>
			</u-form-item>
			
			<u-form-item :required="true" label-width=120rpx label="员工姓名"><u-input class="input1" v-model="form.name" /></u-form-item>
			<u-form-item label="身份证"><u-input class="input" v-model="form.cardId" /></u-form-item>
			<u-form-item label="地址"><u-input class="input" v-model="form.address" /></u-form-item>
			<u-form-item label="邮编"><u-input class="input" v-model="form.postCode" /></u-form-item>
			<u-form-item label="电话"><u-input class="input" v-model="form.tel"  /></u-form-item>
			<u-form-item label="手机"><u-input class="input" v-model="form.phone"  /></u-form-item>
			<u-form-item label="qq号"><u-input class="input" v-model="form.QQNumber"  /></u-form-item>
			<u-form-item label-width=120rpx label="电子邮件"><u-input class="input1" v-model="form.email"  /></u-form-item>
			
			<u-form-item :required="true" label="性别">
				<u-input class="input input2" v-model="form.sex" type="select" border="border" @click="showsex = true" />
				<u-action-sheet :list="actionSheetListsex" v-model="showsex" @click="actionSheetCallbacksex"></u-action-sheet>
			</u-form-item>		
			<u-form-item label-width=120rpx label="政治身份"><u-input class="input1" v-model="form.party"  /></u-form-item>
			
			<!-- 选择日期，用户可以根据下拉框选取年月日 -->
			<view @click="click_birthday">
				<u-form-item label="出生日期" style="font-size:12px;" label-width="80px">
					<view style="width:480rpx;display: flex;flex-direction: row-reverse;">
						<text style="color: #BBBBBB;font-size: 14px;"> {{form.birthday}}</text>
					</view>
					<image src="/static/right.png" style="height: 12px;width: 12px; right: 10px;position:absolute;">
					</image>
				</u-form-item>
			</view>
			
			<u-picker v-model="show_birthday" mode="time" @confirm="save_birthday"></u-picker>
			
			<u-form-item label="民族"><u-input class="input" v-model="form.race"  /></u-form-item>
			<u-form-item label="学历"><u-input class="input" v-model="form.education"  /></u-form-item>
			<u-form-item label="专业"><u-input class="input" v-model="form.speciality"  /></u-form-item>
			<u-form-item label="特长"><u-input class="input" v-model="form.hobby"  /></u-form-item>
			<u-form-item label-width=120rpx label="员工备注"><u-input class="input1" v-model="form.remark"  /></u-form-item>
			
			<!-- 创建日期自动获取当前日期，不需填写 -->
			<u-form-item label-width=120rpx label="创建日期">
				<text class="input1" />{{new Date().toISOString().slice(0, 10)}}</text>
			</u-form-item>
		
		</u-form>
		
		<!-- 确认和取消button -->
		<view class="line btnpos">
			<u-button class="custom-style" :ripple="true" shape="square" size="medium" @click="admit">确定</u-button>
			<u-button class="custom-style1" :ripple="true" shape="square" size="medium" @click="cancel">取消</u-button>
		</view>
	</view>
</template>

<script>
	import helper from '../../common/base.js'
	import currentDate from ' ../..//common/util/currentDate.js';
	export default {
		data() {
			return {
				isConform:false,  //密码是否正确
				
				showsex: false,  //性别下拉框是否显示
				showpos:false,   //职位下拉框是否显示
				showbranch:false,  //部门下拉框是否显示
				actionSheetListsex: [  //性别下拉框信息
					{
						text: '男'
					},
					{
						text: '女'
					}
				],

				department_list: [],
				job_list: [],
				actionSheetListpos: [ //职位下拉框信息，从后端获取

				],
				actionSheetListbranch: [ //部门下拉框信息，从后端获取
				],
				form:{  //添加员工信息表单
					id:'',
					password:'',
					departmentName:'',  
					departmentRemark:'',
					jobName:'',  
					jobRemark:'',
					
					name:'',
					cardId:'', 
					address:'',
					postCode:'',
					tel:'',
					phone:'',
					QQNumber:'',
					email:'',
					sex:'',
					party:'',
					birthday:'',
					race:'',
					education:'',
					speciality:'',
					hobby:'',
					remark:'',
					createDate:new Date().toISOString().slice(0, 10), //自动获取当前日期
					status:''
				},
				uploadsex:'',
				uploadstatus:'',
				show_birthday:false
			}
		},

		onShow(){
			this.department_list=uni.getStorageSync('global_department_list');
			
			this.job_list=uni.getStorageSync('global_job_list');
			
			
			for (let i = 0; i < this.department_list.length; i++) {
				let t = { //构建字典
					"text": ''
				};
				//将部门名字加入部门名称列表actionSheetListbranch中
				t.text = this.department_list[i].departmentName; 
				this.actionSheetListbranch.push(t); 
			}
			
			for (let i = 0; i < this.job_list.length; i++) {
				let t = {
					"text": ''
				};
				//将职位名字加职位名称列表actionSheetListpos中
				t.text = this.job_list[i].jobName;
				this.actionSheetListpos.push(t);
			}
			
		},
		methods: {
			limit(e){
				//长度是否符合
				if(this.form.password.length <8 || this.form.password.length >20 ){
					this.$refs.uToast.show({
						title: '密码格式错误',
						type: 'error'
					})
				}
				let letter=false; //是否有字母
				let number=false; //是否有数字
				for(let i=0;i<this.form.password.length;i++){  
					//是否有数字
					if(this.form.password[i]>="0"&& this.form.password[i]<="9"){
						number=true;
					}
					//是否有字母
					if(this.form.password[i]>="A"&& this.form.password[i]<="Z"){
						letter=true;
					}
					if(this.form.password[i]>="a"&& this.form.password[i]<="z"){
						letter=true;
					}
				}
				if(letter==false || number==false){ //如果没有字母或数字密码格式错误
					this.$refs.uToast.show({
						title: '密码格式错误',
						type: 'error'
					})
					this.isConform=false; 
				}
				else{
					this.isConform=true;
				}
			},
			click_birthday() {
				console.log("click birthday");
				this.show_birthday = true;
			},
			
			//保存出生日期
			save_birthday(e) {
				this.form.birthday = e.year+"年"+e.month+"月"+e.day+"日";
				console.log(this.form.birthday);
				this.show_birthday = false;
			},
			
			//性别选择下拉框函数
			actionSheetCallbacksex(index) {
				this.showsex = true;
				this.form.sex = this.actionSheetListsex[index].text; //将选中的项放入表单
			},
			
			//职位选择下拉框函数
			actionSheetCallbackpos(index) {
				this.showpos = true;
				this.form.jobName = this.actionSheetListpos[index].text; //将选中的项放入表单
				this.form.jobRemark = this.job_list[index].jobRemark;
				console.log(this.job_list[index].jobRemark);
			},
			
			//部门选择下拉框函数
			actionSheetCallbackbranch(index) {
				this.showbranch = true;
				this.form.departmentName = this.actionSheetListbranch[index].text;
				this.form.departmentRemark = this.department_list[index].departmentRemark; //将选中的项放入表单
			},
			
			//确认提交函数
			admit(){
				if (this.form.sex && this.form.id && this.isConform && this.form.name && this.form.departmentName && this.form.jobName && this.form.createDate){
					if (this.form.sex == '男') {
						this.uploadsex = '1';
					} else {
						this.uploadsex = '2';
					}

					uni.request({
						url: helper.websiteUrl+ '/employee/append', //添加员工接口
						method: 'POST',
						data:{      //post请求发送employee类信息
							"id": this.form.id,
							"password": this.form.password,
							"departmentName": this.form.departmentName,
							"departmentRemark": this.form.departmentRemark,
							"jobName": this.form.jobName,
							"jobRemark": this.form.jobRemark,
							
							"name": this.form.name,
							"cardId": this.form.cardId,
							"address": this.form.address,
							"postCode": this.form.postCode,
							"tel": this.form.tel,
							"phone": this.form.phone,
							"QQNumber": this.form.QQNumber,
							"email": this.form.email,
							"sex": this.uploadsex,
							"party": this.form.party,
							"birthday": this.form.birthday,
							"race": this.form.race,
							"education": this.form.education,
							"speciality": this.form.speciality,
							"hobby": this.form.hobby,
							"remark": this.form.remark,
							"createDate": this.form.createDate,
							"status": '0'
						},
						header: {
							"token": uni.getStorageSync('token')
						},
						success: (res) => {
							if (res.data.code == 200){ //添加员工成功
								console.log(res.data);
								this.$refs.uToast.show({ 
									title: '添加员工成功',
									type: 'success',
									duration:600
								})
								
								uni.request({
									url: helper.websiteUrl+'/employee/getAll',
									method: 'GET',
									header: {
										"token": uni.getStorageSync('token')
									},
									success: (res) => {
										if (res.data.code == 200){
											uni.setStorageSync('global_employee_list',res.data.data);
										}
										else{
											this.$refs.uToast.show({
												title: '获取员工信息失败',
												type: 'error'
											})
										}
									}
								});
								
							}
							else{
								this.$refs.uToast.show({  //添加员工失败
									title: '添加员工失败',
									type: 'error',
									duration:600
								})
							}
							setTimeout(()=>{
								uni.navigateBack({
								})
							},200);
						}
					});
				}
				else{
					this.$refs.uToast.show({  //提示必选项未填写完整
						title: '必填项未填写完整',
						type: 'error'
					})
				}
			},
			cancel(){  //点击取消回到员工首页
				uni.navigateBack({
					
				})
			}
		}
	}
</script>

<style scoped>
	/* 按钮颜色设置 */
	.custom-style {
		background-color: #9EC2EC;
	}
	
	.custom-style1 {
		background-color:#A994FB;
	}
	
	.input{
		width:20px;
		margin-left: 30px;
	}
	
	/* 设置输入字体格式 */
	.input1{     
		width:20px;
		margin-left: 17px;
	}
	
	/* 设置输入字体格式 */
	.input2{
		margin-right: 10px;
	}
	
	/* 排列在一行 */
	.line{
		display: flex;
		flex-direction: row;
	}
	
	/* 按钮的位置 */
	.btnpos{
	  margin-top: 20px;
	  width: 100%;
	}
</style>
