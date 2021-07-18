<template>
	<view>
		<view>
			<u-toast ref="uToast" />
		</view>
		
		<!-- 修改员工信息表单 -->
		<u-form style="margin-left:10px;" :model="form" ref="uForm">
			<u-form-item label="ID" style="font-size:16px;" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<text style="color: #BBBBBB;font-size: 16px;"> {{form.id}}</text>
				</view>
			</u-form-item>
			
			<u-form-item label="创建时间" style="font-size:16px;" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<text style="color: #BBBBBB;font-size: 16px;"> {{form.createDate}}</text>
				</view>
			</u-form-item>
		</u-form>
		<u-gap height="30" bg-color="#f3f4f6"></u-gap>

		<u-form style="margin-left:10px;" :model="form" ref="uForm">

			<view @click="click_name">
				<u-form-item label="姓名" style="font-size:16px;" label-width="80px">
					<view style="width:480rpx;display: flex;flex-direction: row-reverse;">
						<text style="color: #BBBBBB;font-size: 16px;"> {{form.name}}</text>
					</view>
					<image src="/static/right.png" style="height: 13px;width: 13px; right: 10px;position:absolute;">
					</image>
				</u-form-item>
			</view>

			<view @click="click_sex">
				<u-form-item label="性别" style="font-size:16px;" label-width="80px">
					<view style="width:480rpx;display: flex;flex-direction: row-reverse;">
						<text style="color: #BBBBBB;font-size: 16px;"> {{sex}}</text>
					</view>
					<image src="/static/right.png" style="height: 13px;width: 13px; right: 10px;position:absolute;">
					</image>
				</u-form-item>
			</view>

			<view @click="click_phone">
				<u-form-item label="手机" style="font-size:16px;" label-width="80px">
					<view style="width:480rpx;display: flex;flex-direction: row-reverse;">
						<text style="color: #BBBBBB;font-size: 16px;"> {{phone}}</text>
					</view>
					<image src="/static/right.png" style="height: 13px;width: 13px; right: 10px;position:absolute;">
					</image>
				</u-form-item>
			</view>

			<view @click="click_cardId">
				<u-form-item label="身份证" style="font-size:16px;" label-width="80px">
					<view style="width:480rpx;display: flex;flex-direction: row-reverse;">
						<text style="color: #BBBBBB;font-size: 16px;"> {{cardId}}</text>
					</view>
					<image src="/static/right.png" style="height: 13px;width: 13px; right: 10px;position:absolute;">
					</image>
				</u-form-item>
			</view>
		</u-form>
		<u-gap height="30" bg-color="#f3f4f6"></u-gap>

		<u-form style="margin-left:10px;" :model="form" ref="uForm">

			<view @click="click_departmentName">
				<u-form-item label="部门" style="font-size:16px;" label-width="80px">
					<view style="width:480rpx;display: flex;flex-direction: row-reverse;">
						<text style="color: #BBBBBB;font-size: 16px;"> {{form.departmentName}}</text>
					</view>
					<image src="/static/right.png" style="height: 13px;width: 13px; right: 10px;position:absolute;">
					</image>
				</u-form-item>
			</view>

			<u-form-item label="部门信息" style="font-size:16px;" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<textarea :value="form.departmentRemark" style="color: #BBBBBB;font-size: 16px;" :disabled=true
						:auto-height=true></textarea>

				</view>
			</u-form-item>

			<view @click="click_jobName">
				<u-form-item label="职位" style="font-size:16px;" label-width="80px">
					<view style="width:480rpx;display: flex;flex-direction: row-reverse;">
						<text style="color: #BBBBBB;font-size: 16px;"> {{form.jobName}}</text>
					</view>
					<image src="/static/right.png" style="height: 13px;width: 13px; right: 10px;position:absolute;">
					</image>
				</u-form-item>
			</view>

			<u-form-item label="职位信息" style="font-size:16px;" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<textarea :value="form.jobRemark" style="color: #BBBBBB;font-size: 16px;" :disabled=true
						:auto-height=true></textarea>

				</view>
			</u-form-item>

		</u-form>
		<u-gap height="30" bg-color="#f3f4f6"></u-gap>

		<u-form style="margin-left:10px;" :model="form" ref="uForm">
			<view @click="click_race">
				<u-form-item label="民族" style="font-size:16px;" label-width="80px">
					<view style="width:480rpx;display: flex;flex-direction: row-reverse;">
						<text style="color: #BBBBBB;font-size: 16px;"> {{race}}</text>
					</view>
					<image src="/static/right.png" style="height: 13px;width: 13px; right: 10px;position:absolute;">
					</image>
				</u-form-item>
			</view>

			<view @click="click_education">
				<u-form-item label="学历" style="font-size:16px;" label-width="80px">
					<view style="width:480rpx;display: flex;flex-direction: row-reverse;">
						<text style="color: #BBBBBB;font-size: 16px;"> {{education}}</text>
					</view>
					<image src="/static/right.png" style="height: 13px;width: 13px; right: 10px;position:absolute;">
					</image>
				</u-form-item>
			</view>

			<view @click="click_speciality">
				<u-form-item label="专业" style="font-size:16px;" label-width="80px">
					<view style="width:480rpx;display: flex;flex-direction: row-reverse;">
						<text style="color: #BBBBBB;font-size: 16px;"> {{speciality}}</text>
					</view>
					<image src="/static/right.png" style="height: 13px;width: 13px; right: 10px;position:absolute;">
					</image>
				</u-form-item>
			</view>

			<view @click="click_party">
				<u-form-item label="政治身份" style="font-size:16px;" label-width="80px">
					<view style="width:480rpx;display: flex;flex-direction: row-reverse;">
						<text style="color: #BBBBBB;font-size: 16px;"> {{party}}</text>
					</view>
					<image src="/static/right.png" style="height: 13px;width: 13px; right: 10px;position:absolute;">
					</image>
				</u-form-item>
			</view>

			<view @click="click_birthday">
				<u-form-item label="出生日期" style="font-size:16px;" label-width="80px">
					<view style="width:480rpx;display: flex;flex-direction: row-reverse;">
						<text style="color: #BBBBBB;font-size: 16px;"> {{birthday}}</text>
					</view>
					<image src="/static/right.png" style="height: 13px;width: 13px; right: 10px;position:absolute;">
					</image>
				</u-form-item>
			</view>
		</u-form>
		<u-gap height="30" bg-color="#f3f4f6"></u-gap>

		<u-form style="margin-left:10px;" :model="form" ref="uForm">

			<u-form-item label="住址" style="font-size:16px;" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<text style="color: #BBBBBB;font-size: 16px;"> {{form.address}}</text>
				</view>
			</u-form-item>

			<u-form-item label="邮编" style="font-size:16px;" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<text style="color: #BBBBBB;font-size: 16px;"> {{form.postCode}}</text>
				</view>
			</u-form-item>

			<u-form-item label="电话" style="font-size:16px;" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<text style="color: #BBBBBB;font-size: 16px;"> {{form.tel}}</text>
				</view>
			</u-form-item>

			<u-form-item label="QQ" style="font-size:16px;" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<text style="color: #BBBBBB;font-size: 16px;"> {{form.QQNumber}}</text>
				</view>
			</u-form-item>

			<u-form-item label="电子邮件" style="font-size:16px;" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<text style="color: #BBBBBB;font-size: 16px;"> {{form.email}}</text>
				</view>
			</u-form-item>

			<u-form-item label="特长" style="font-size:16px;" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<text style="color: #BBBBBB;font-size: 16px;"> {{form.hobby}}</text>
				</view>
			</u-form-item>

			<u-form-item label="备注" style="font-size:16px;" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<text style="color: #BBBBBB;font-size: 16px;"> {{form.remark}}</text>
				</view>
			</u-form-item>
		</u-form>

		<view>
			<u-toast ref="uToast" />
		</view>

		<!-- 弹出层 -->
		<view>
			<u-popup v-model="show_name" mode="top" height="400rpx">
				<view style="margin-top: 5%;">
					<text style="font-size: 20px;margin-left: 39%;">编辑姓名</text>
				</view>

				<view style="display: flex;flex-direction: row;margin-top: 9%;">
					<text style="font-size: 15px;margin-left: 10%;margin-top: 1%;">姓名</text>
					<input v-model="name" class="inputText" type="text"
						style="border-radius: 5px;padding-left: 10px;" />
				</view>

				<u-button size="medium " style="margin-left: 37%;margin-top: 7%;" :ripple="true" @click="save_name">
					保存</u-button>
			</u-popup>
		</view>

		<view>
			<u-popup v-model="show_sex" mode="top" height="400rpx">
				<view style="margin-top: 5%;">
					<text style="font-size: 20px;margin-left: 39%;">编辑性别</text>
				</view>

				<view style="display: flex;flex-direction: row;margin-top: 9%;">
					<text style="font-size: 15px;margin-left: 10%;margin-top: 1%;">性别</text>

					<u-radio-group v-model="sex" @change="radioGroupChange" style="padding-left: 22%;">
						<u-radio @change="radioChange" v-for="(item, index) in sex_list" :key="index" :name="item.name"
							:disabled="item.disabled">
							{{item.name}}
						</u-radio>
					</u-radio-group>

				</view>

				<u-button size="medium " style="margin-left: 37%;margin-top: 7%;" :ripple="true" @click="save_sex">
					保存</u-button>
			</u-popup>
		</view>

		<view>
			<u-popup v-model="show_phone" mode="top" height="400rpx">
				<view style="margin-top: 5%;">
					<text style="font-size: 20px;margin-left: 39%;">编辑手机</text>
				</view>

				<view style="display: flex;flex-direction: row;margin-top: 9%;">
					<text style="font-size: 15px;margin-left: 10%;margin-top: 1%;">手机</text>
					<input v-model="phone" class="inputText" type="text"
						style="border-radius: 5px;padding-left: 10px;" />
				</view>

				<u-button size="medium " style="margin-left: 37%;margin-top: 7%;" :ripple="true" @click="save_phone">
					保存</u-button>
			</u-popup>
		</view>

		<view>
			<u-popup v-model="show_cardId" mode="top" height="400rpx">
				<view style="margin-top: 5%;">
					<text style="font-size: 20px;margin-left: 39%;">编辑身份证</text>
				</view>

				<view style="display: flex;flex-direction: row;margin-top: 9%;">
					<text style="font-size: 15px;margin-left: 10%;margin-top: 1%;">身份证</text>
					<input v-model="cardId" class="inputText" type="text"
						style="border-radius: 5px;padding-left: 10px;" />
				</view>

				<u-button size="medium " style="margin-left: 37%;margin-top: 7%;" :ripple="true" @click="save_cardId">
					保存</u-button>
			</u-popup>
		</view>

		<view>
			<u-popup v-model="show_password" mode="top" height="400rpx">
				<view style="margin-top: 5%;">
					<text style="font-size: 20px;margin-left: 39%;">编辑密码</text>
				</view>

				<view style="display: flex;flex-direction: row;margin-top: 9%;">
					<text style="font-size: 15px;margin-left: 10%;margin-top: 1%;">密码</text>
					<input v-model="password" class="inputText" type="text"
						style="border-radius: 5px;padding-left: 10px;" />
				</view>

				<u-button size="medium " style="margin-left: 37%;margin-top: 7%;" :ripple="true" @click="save_password">
					保存</u-button>
			</u-popup>
		</view>

		<u-select v-model="show_departmentName" mode="single-column" :list="departmentName_list"
			@confirm="confirm_department"></u-select>

		<u-select v-model="show_jobName" mode="single-column" :list="jobName_list" @confirm="confirm_job"></u-select>

		<view>
			<u-popup v-model="show_race" mode="top" height="400rpx">
				<view style="margin-top: 5%;">
					<text style="font-size: 20px;margin-left: 39%;">编辑民族</text>
				</view>

				<view style="display: flex;flex-direction: row;margin-top: 9%;">
					<text style="font-size: 15px;margin-left: 10%;margin-top: 1%;">民族</text>
					<input v-model="race" class="inputText" type="text"
						style="border-radius: 5px;padding-left: 10px;" />
				</view>

				<u-button size="medium " style="margin-left: 37%;margin-top: 7%;" :ripple="true" @click="save_race">
					保存</u-button>
			</u-popup>
		</view>

		<view>
			<u-popup v-model="show_education" mode="top" height="400rpx">
				<view style="margin-top: 5%;">
					<text style="font-size: 20px;margin-left: 39%;">编辑学历</text>
				</view>

				<view style="display: flex;flex-direction: row;margin-top: 9%;">
					<text style="font-size: 15px;margin-left: 10%;margin-top: 1%;">学历</text>
					<input v-model="education" class="inputText" type="text"
						style="border-radius: 5px;padding-left: 10px;" />
				</view>

				<u-button size="medium " style="margin-left: 37%;margin-top: 7%;" :ripple="true"
					@click="save_education">
					保存</u-button>
			</u-popup>
		</view>

		<view>
			<u-popup v-model="show_speciality" mode="top" height="400rpx">
				<view style="margin-top: 5%;">
					<text style="font-size: 20px;margin-left: 39%;">编辑专业</text>
				</view>

				<view style="display: flex;flex-direction: row;margin-top: 9%;">
					<text style="font-size: 15px;margin-left: 10%;margin-top: 1%;">专业</text>
					<input v-model="speciality" class="inputText" type="text"
						style="border-radius: 5px;padding-left: 10px;" />
				</view>

				<u-button size="medium " style="margin-left: 37%;margin-top: 7%;" :ripple="true"
					@click="save_speciality">
					保存</u-button>
			</u-popup>
		</view>

		<view>
			<u-popup v-model="show_party" mode="top" height="400rpx">
				<view style="margin-top: 5%;">
					<text style="font-size: 20px;margin-left: 34%;">编辑政治身份</text>
				</view>

				<view style="display: flex;flex-direction: row;margin-top: 9%;">
					<text style="font-size: 15px;margin-left: 4%;margin-top: 1%;">政治身份</text>
					<input v-model="party" class="inputText" type="text"
						style="border-radius: 5px;padding-left: 10px;" />
				</view>

				<u-button size="medium " style="margin-left: 37%;margin-top: 7%;" :ripple="true" @click="save_party">
					保存</u-button>
			</u-popup>
		</view>

		<view>
			<u-picker v-model="show_birthday" mode="time" @confirm="save_birthday"></u-picker>
		</view>

	</view>
</template>

<script>
	import helper from '../../common/base.js'
	export default {
		data() {
			return {
				id:'',
				name: '',
				sex: '',
				phone: '',
				cardId: '',
				password: '',
				departmentName: '',
				departmentRemark: '',
				jobName: '',
				jobRemark: '',
				race: '',
				education: '',
				speciality: '',
				party: '',
				birthday: '',
				show_name: false,
				show_sex: false,
				show_phone: false,
				show_cardId: false,
				show_password: false,
				show_departmentName: false,
				show_jobName: false,
				show_race: false,
				show_education: false,
				show_speciality: false,
				show_party: false,
				show_birthday: false,
				form: {},
				sex_list: [{   //性别
						name: '男',
						disabled: false
					},
					{
						name: '女',
						disabled: false
					}
				],
				department_list: [ //部门列表，从后端获取

				],
				job_list: [], //职位列表，从后端获取
				departmentName_list: [  //部门名称列表
				],
				jobName_list: []  //职位名称列表
			}
		},
		
		onShow() {
			//由用户ID获取该用户的全部信息
			uni.request({
				url: helper.websiteUrl+'/employee/myId', 
				data: {
					"id": uni.getStorageSync('empolyeeId')
				},
				header: {
					"token": uni.getStorageSync('token') //向后端传输token
				},
				method: 'POST',
				heads: {
					'content-type': 'application/x-www-form-urlencoded'
				},
				success: (res) => {
					console.log(this.form.status);
					if (res.data.code == 200) {
						this.form = res.data.data;
						this.name = this.form.name;
						//如果性别数据为2，为女
						if (this.form.sex == "2") { 
							this.sex = '女';
						} else {
							this.sex = '男';
						}
						this.phone = this.form.phone;
						this.cardId = this.form.cardId;
						this.departmentName = this.form.departmentName;
						this.jobName = this.form.jobName;
						this.race = this.form.race;
						this.education = this.form.education;
						this.speciality = this.form.speciality;
						this.party = this.form.party;
						this.birthday = this.form.birthday;
					} else {
						this.$refs.uToast.show({
							title: '获取个人信息失败',
							type: 'error'
						})
					}
				}
			});
			
			this.department_list=uni.getStorageSync('global_department_list');
			
			for (let i = 0; i < this.department_list.length; i++) {
				//构建字典，以满足u-view组件格式
				let t = {
					"label": '',
					"index": ''
				};
				t.label = this.department_list[i].departmentName; //赋值部门名称
				t.index = i;  //赋值部门索引
				this.departmentName_list.push(t); //向部门名称列表中加入
			}
			
			this.job_list = uni.getStorageSync('global_job_list');
			
			for (let i = 0; i < this.job_list.length; i++) {
				//构建字典，以满足u-view组件格式
				let t = {
					"label": '',
					"index": ''
				};
				t.label = this.job_list[i].jobName; //赋值职位名称
				t.index = i;   //赋值职位索引
				this.jobName_list.push(t);  //向职位名称列表中加入
			}
		},
		onBackPress(){
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
			setTimeout(()=>{
				uni.redirectTo({
					url:'/pages/employee/employee'
				})
			},200);
			return true;
		},
		methods: {
			//确认部门
			confirm_department(e) {
				console.log(e);
				this.form.departmentName = e[0].label;
				for (let i = 0; i < this.department_list.length; i++) {
					if (this.department_list[i].departmentName == e[0].label) {
						this.form.departmentRemark = this.department_list[i].departmentRemark;
						break;
					}
				}
				this.change(); //触发更改事件
			},
			//确认职业
			confirm_job(e) {
				console.log(e);
				this.form.jobName = e[0].label;
				for (let i = 0; i < this.job_list.length; i++) {
					if (this.job_list[i].jobName == e[0].label) {
						this.form.jobRemark = this.job_list[i].jobRemark;
						break;
					}
				}
				this.change(); //触发更改事件
			},
			radioChange(e) {
				//console.log(e);
			},
			radioGroupChange(e) {
				//console.log(e);
			},
			
			//更改事件
			change() {
				console.log('change');
				uni.request({
					url: helper.websiteUrl+'/employee/change',
					data: {  //向后端传送表单Employee类所有信息
						"id": this.form.id,
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
						"sex": this.form.sex,
						"party": this.form.party,
						"birthday": this.form.birthday,
						"race": this.form.race,

						"education": this.form.education,
						"speciality": this.form.speciality,
						"hobby": this.form.hobby,
						"remark": this.form.remark,
						"createDate": this.form.createDate,
						"status": this.form.status
					},
					method: 'POST',
					heads: {
						'content-type': 'application/x-www-form-urlencoded'
					},
					header: {
						"token": uni.getStorageSync('token')
					},
					success: (res) => {
						if (res.data.code == 200) {
							console.log(res.data);
						} else {
							this.$refs.uToast.show({
								title: '修改员工信息失败',
								type: 'error'
							})
						}
					}
				})
			},
			
			//保存名字
			save_name() {
				this.form.name = this.name;
				console.log(this.form.name);
				this.show_name = false;
				this.change();
			},
			
			//保存性别
			save_sex() {
				if (this.sex == "男") {
					this.form.sex = "1";
				} else {
					this.form.sex = "2";
				}
				console.log(this.form.sex);
				this.show_sex = false;
				this.change();
			},
			
			//保存手机
			save_phone() {
				this.form.phone = this.phone;
				console.log(this.form.phone);
				this.show_phone = false;
				this.change();
			},
			
			//保存身份证
			save_cardId() {
				this.form.cardId = this.cardId;
				console.log(this.form.cardId);
				this.show_cardId = false;
				this.change();
			},
			
			//保存密码
			save_password() {
				this.form.password = this.password;
				console.log(this.form.password);
				this.show_password = false;
				this.change();
			},
			
			//保存部门名称
			save_departmentName() {
				this.form.departmentName = this.departmentName;
				console.log(this.form.departmentName);
				this.show_departmentName = false;
				this.change();

			},
			
			//保存职位名称
			save_jobName() {
				this.form.jobName = this.jobName;
				console.log(this.form.jobName);
				this.show_jobName = false;
				this.change();

			},
			
			//保存民族
			save_race() {
				this.form.race = this.race;
				console.log(this.form.race);
				this.show_race = false;
				this.change();
			},
			
			//保存学历
			save_education() {
				this.form.education = this.education;
				console.log(this.form.education);
				this.show_education = false;
				this.change();
			},
			
			//保存特长
			save_speciality() {
				this.form.speciality = this.speciality;
				console.log(this.form.speciality);
				this.show_speciality = false;
				this.change();
			},
			
			//保存身份
			save_party() {
				this.form.party = this.party;
				console.log(this.form.party);
				this.show_party = false;
				this.change();
			},
			
			//保存出生日期
			save_birthday(e) {
				this.birthday=e.year+"年"+e.month+"月"+e.day+"日";
				this.form.birthday = this.birthday;
				console.log(this.form.birthday);
				this.show_birthday = false;
				this.change();
			},
			
			click_name() {
				console.log("click name");
				this.show_name = true;
			},
			click_sex() {
				console.log("click sex");
				this.show_sex = true;
			},
			click_phone() {
				console.log("click phone");
				this.show_phone = true;
			},
			click_cardId() {
				console.log("click cardId");
				this.show_cardId = true;
			},
			click_password() {
				console.log("click password");
				this.show_password = true;
			},
			click_departmentName() {
				console.log("click departmentName");
				this.show_departmentName = true;
			},

			click_jobName() {
				console.log("click jobName");
				this.show_jobName = true;
			},

			click_race() {
				console.log("click race");
				this.show_race = true;
			},
			click_education() {
				console.log("click education");
				this.show_education = true;
			},
			click_speciality() {
				console.log("click speciality");
				this.show_speciality = true;
			},
			click_party() {
				console.log("click party");
				this.show_party = true;
			},
			click_birthday() {
				console.log("click birthday");
				this.show_birthday = true;
			}
		}
	}
</script>

<style>
	.inputText {
		width: 450rpx;
		height: 60rpx;
		border-radius: true;
		background-color: #efefef;
		margin-left: 6%;
	}
</style>
