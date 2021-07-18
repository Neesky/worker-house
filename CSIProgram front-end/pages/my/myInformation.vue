<template>
	<!-- <u-form-item label="密码"><text class="input" >{{form.password}}</text></u-form-item> -->
	<!-- <image src="/static/right.png" style="height: 13px;width: 13px;right: 10px;position:absolute; margin-top: 3%;" ></image> -->
	<view>
		<u-form style="margin-left:10px;" :model="form" ref="uForm">
			<u-form-item label="姓名" style="font-size:16px;" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<text style="color: #BBBBBB;font-size: 16px;"> {{form.name}}</text>
				</view>
			</u-form-item>

			<u-form-item label="性别" style="font-size:16px;" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<text style="color: #BBBBBB;font-size: 16px;"> {{sex}}</text>
				</view>
			</u-form-item>

			<u-form-item label="手机" style="font-size:16px;" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<text style="color: #BBBBBB;font-size: 16px;"> {{form.phone}}</text>
				</view>
			</u-form-item>

			<u-form-item label="身份证" style="font-size:16px;" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<text style="color: #BBBBBB;font-size: 16px;"> {{form.cardId}}</text>
				</view>
			</u-form-item>
		</u-form>
		<u-gap height="30" bg-color="#f3f4f6"></u-gap>

		<u-form style="margin-left:10px;" :model="form" ref="uForm">
			<u-form-item label="ID" style="font-size:16px;" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<text style="color: #BBBBBB;font-size: 16px;"> {{form.id}}</text>
				</view>
			</u-form-item>

			<u-form-item label="部门" style="font-size:16px;" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<text style="color: #BBBBBB;font-size: 16px;"> {{form.departmentName}}</text>
				</view>
			</u-form-item>

<!-- 			<u-form-item label="部门信息" style="font-size:16px;" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<text style="color: #BBBBBB;font-size: 16px;"> {{form.departmentRemark}}</text>
				</view>
			</u-form-item> -->
			<u-form-item label="部门信息" style="font-size:16px;" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<textarea :value="form.departmentRemark" style="color: #BBBBBB;font-size: 16px;" :disabled=true
						:auto-height=true></textarea>
				</view>
			</u-form-item>

			<u-form-item label="职位" style="font-size:16px;" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<text style="color: #BBBBBB;font-size: 16px;"> {{form.jobName}}</text>
				</view>
			</u-form-item>

			<u-form-item label="职位信息" style="font-size:16px;" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<textarea :value="form.jobRemark" style="color: #BBBBBB;font-size: 16px;" :disabled=true
						:auto-height=true></textarea>
				</view>
			</u-form-item>
			<!-- <u-form-item label="职位信息" style="font-size:16px;" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<text style="color: #BBBBBB;font-size: 16px;"> {{form.jobRemark}}</text>
				</view>
			</u-form-item> -->
		</u-form>
		<u-gap height="30" bg-color="#f3f4f6"></u-gap>

		<u-form style="margin-left:10px;" :model="form" ref="uForm">
			<u-form-item label="民族" style="font-size:16px;" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<text style="color: #BBBBBB;font-size: 16px;"> {{form.race}}</text>
				</view>
			</u-form-item>

			<u-form-item label="学历" style="font-size:16px;" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<text style="color: #BBBBBB;font-size: 16px;"> {{form.education}}</text>
				</view>
			</u-form-item>

			<u-form-item label="专业" style="font-size:16px;" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<text style="color: #BBBBBB;font-size: 16px;"> {{form.speciality}}</text>
				</view>
			</u-form-item>

			<u-form-item label="政治身份" style="font-size:16px;" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<text style="color: #BBBBBB;font-size: 16px;"> {{form.party}}</text>
				</view>
			</u-form-item>

			<u-form-item label="出生日期" style="font-size:16px;" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<text style="color: #BBBBBB;font-size: 16px;"> {{form.birthday}}</text>
				</view>
			</u-form-item>
		</u-form>
		<u-gap height="30" bg-color="#f3f4f6"></u-gap>

		<u-form style="margin-left:10px;" :model="form" ref="uForm">
			<view @click="click_address">
				<u-form-item label="住址" style="font-size:16px;" label-width="80px">
					<view style="width:480rpx;display: flex;flex-direction: row-reverse;">
						<text style="color: #BBBBBB;font-size: 16px;"> {{form.address}}</text>
					</view>
					<image src="/static/right.png" style="height: 13px;width: 13px; right: 10px;position:absolute;">
					</image>
				</u-form-item>
			</view>

			<view @click="click_postCode">
				<u-form-item label="邮编" style="font-size:16px;" label-width="80px">
					<view style="width:480rpx;display: flex;flex-direction: row-reverse;">
						<text style="color: #BBBBBB;font-size: 16px;"> {{form.postCode}}</text>
					</view>
					<image src="/static/right.png" style="height: 13px;width: 13px; right: 10px;position:absolute;">
					</image>
				</u-form-item>
			</view>

			<view @click="click_tel">
				<u-form-item label="电话" style="font-size:16px;" label-width="80px">
					<view style="width:480rpx;display: flex;flex-direction: row-reverse;">
						<text style="color: #BBBBBB;font-size: 16px;"> {{form.tel}}</text>
					</view>
					<image src="/static/right.png" style="height: 13px;width: 13px; right: 10px;position:absolute;">
					</image>
				</u-form-item>
			</view>

			<view @click="click_QQNumber">
				<u-form-item label="QQ" style="font-size:16px;" label-width="80px">
					<view style="width:480rpx;display: flex;flex-direction: row-reverse;">
						<text style="color: #BBBBBB;font-size: 16px;"> {{form.QQNumber}}</text>
					</view>
					<image src="/static/right.png" style="height: 13px;width: 13px; right: 10px;position:absolute;">
					</image>
				</u-form-item>
			</view>


			<view @click="click_email">
				<u-form-item label="电子邮件" style="font-size:16px;" label-width="80px">
					<view style="width:480rpx;display: flex;flex-direction: row-reverse;">
						<text style="color: #BBBBBB;font-size: 16px;"> {{form.email}}</text>
					</view>
					<image src="/static/right.png" style="height: 13px;width: 13px; right: 10px;position:absolute;">
					</image>
				</u-form-item>
			</view>

			<view @click="click_hobby">
				<u-form-item label="特长" style="font-size:16px;" label-width="80px">
					<view style="width:480rpx;display: flex;flex-direction: row-reverse;">
						<text style="color: #BBBBBB;font-size: 16px;"> {{form.hobby}}</text>
					</view>
					<image src="/static/right.png" style="height: 13px;width: 13px; right: 10px;position:absolute;">
					</image>
				</u-form-item>
			</view>

			<view @click="click_remark">
				<u-form-item label="备注" style="font-size:16px;" label-width="80px">
					<view style="width:480rpx;display: flex;flex-direction: row-reverse;">
						<text style="color: #BBBBBB;font-size: 16px;"> {{form.remark}}</text>
					</view>
					<image src="/static/right.png" style="height: 13px;width: 13px; right: 10px;position:absolute;">
					</image>
				</u-form-item>
			</view>
		</u-form>
		<u-gap height="30" bg-color="#f3f4f6"></u-gap>

		<u-form style="margin-left:10px;" :model="form" ref="uForm">
			<u-form-item label="用户状态" style="font-size:16px;" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<text style="color: #BBBBBB;font-size: 16px;"> {{user_status}}</text>
				</view>
			</u-form-item>
		</u-form>
		<u-form style="margin-left:10px;" :model="form" ref="uForm">
			<u-form-item label="创建时间" style="font-size:16px;" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<text style="color: #BBBBBB;font-size: 16px;"> {{form.createDate}}</text>
				</view>
			</u-form-item>
		</u-form>

		<view>
			<u-toast ref="uToast" />
		</view>

		<view>
			<u-popup v-model="show_address" mode="top" height="400rpx">
				<view style="margin-top: 5%;">
					<text style="font-size: 20px;margin-left: 39%;">更改地址</text>
				</view>

				<view style="display: flex;flex-direction: row;margin-top: 9%;">
					<text style="font-size: 15px;margin-left: 10%;margin-top: 1%;">地址</text>
					<input v-model="address" class="inputText" type="text" style="border-radius: 5px;padding-left: 10px;"/>
				</view>

				<u-button size="medium " style="margin-left: 37%;margin-top: 7%;" :ripple="true" @click="save_address">
					保存</u-button>
			</u-popup>
		</view>
		
		<view>
			<u-popup v-model="show_postCode" mode="top" height="400rpx">
				<view style="margin-top: 5%;">
					<text style="font-size: 20px;margin-left: 39%;">更改邮编</text>
				</view>
		
				<view style="display: flex;flex-direction: row;margin-top: 9%;">
					<text style="font-size: 15px;margin-left: 10%;margin-top: 1%;">邮编</text>
					<input v-model="postCode" class="inputText" type="text" style="border-radius: 5px;padding-left: 10px;" />
				</view>
		
				<u-button size="medium " style="margin-left: 37%;margin-top: 7%;" :ripple="true" @click="save_postCode">
					保存</u-button>
			</u-popup>
		</view>
		
		<view>
			<u-popup v-model="show_tel" mode="top" height="400rpx">
				<view style="margin-top: 5%;">
					<text style="font-size: 20px;margin-left: 39%;">更改电话</text>
				</view>
		
				<view style="display: flex;flex-direction: row;margin-top: 9%;">
					<text style="font-size: 15px;margin-left: 10%;margin-top: 1%;">电话</text>
					<input v-model="tel" class="inputText" type="text" style="border-radius: 5px;padding-left: 10px;"/>
				</view>
		
				<u-button size="medium " style="margin-left: 37%;margin-top: 7%;" :ripple="true" @click="save_tel">
					保存</u-button>
			</u-popup>
		</view>
		
		<view>
			<u-popup v-model="show_QQNumber" mode="top" height="400rpx">
				<view style="margin-top: 5%;">
					<text style="font-size: 20px;margin-left: 39%;">更改QQ</text>
				</view>
		
				<view style="display: flex;flex-direction: row;margin-top: 9%;">
					<text style="font-size: 15px;margin-left: 10%;margin-top: 1%;">QQ</text>
					<input v-model="QQNumber" class="inputText" type="text" style="border-radius: 5px;padding-left: 10px;"/>
				</view>
		
				<u-button size="medium " style="margin-left: 37%;margin-top: 7%;" :ripple="true" @click="save_QQNumber">
					保存</u-button>
			</u-popup>
		</view>
		
		<view>
			<u-popup v-model="show_email" mode="top" height="400rpx">
				<view style="margin-top: 5%;">
					<text style="font-size: 20px;margin-left: 36%;">更改电子邮件</text>
				</view>
		
				<view style="display: flex;flex-direction: row;margin-top: 9%;">
					<text style="font-size: 15px;margin-left: 6%;margin-top: 1%;">电子邮件</text>
					<input v-model="email" class="inputText" type="text" style="border-radius: 5px;padding-left: 10px;"/>
				</view>
		
				<u-button size="medium " style="margin-left: 37%;margin-top: 7%;" :ripple="true" @click="save_email">
					保存</u-button>
			</u-popup>
		</view>

		<view>
			<u-popup v-model="show_hobby" mode="top" height="400rpx">
				<view style="margin-top: 5%;">
					<text style="font-size: 20px;margin-left: 39%;">更改特长</text>
				</view>
		
				<view style="display: flex;flex-direction: row;margin-top: 9%;">
					<text style="font-size: 15px;margin-left: 10%;margin-top: 1%;">特长</text>
					<input v-model="hobby" class="inputText" type="text" style="border-radius: 5px;padding-left: 10px;"/>
				</view>
		
				<u-button size="medium " style="margin-left: 37%;margin-top: 7%;" :ripple="true" @click="save_hobby">
					保存</u-button>
			</u-popup>
		</view>
		
		<view>
			<u-popup v-model="show_remark" mode="top" height="400rpx">
				<view style="margin-top: 5%;">
					<text style="font-size: 20px;margin-left: 39%;">更改备注</text>
				</view>
		
				<view style="display: flex;flex-direction: row;margin-top: 9%;">
					<text style="font-size: 15px;margin-left: 10%;margin-top: 1%;">备注</text>
					<input v-model="remark" class="inputText" type="text" style="border-radius: 5px;padding-left: 10px;"/>
				</view>
		
				<u-button size="medium " style="margin-left: 37%;margin-top: 7%;" :ripple="true" @click="save_remark">
					保存</u-button>
			</u-popup>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				user_status:'普通用户',
				address: '',
				postCode: '',
				tel: '',
				QQNumber: '',
				email: '',
				hobby: '',
				remark: '',
				show_address: false,
				show_postCode: false,
				show_tel: false,
				show_QQNumber: false,
				show_email: false,
				show_hobby: false,
				show_remark: false,
				form: {},
				sex: ''
			}
		},
		onLoad() {
			console.log('on load');
			console.log(uni.getStorageSync('global_status'));
			if(uni.getStorageSync('global_status')=='1'){
				this.user_status='管理员';
			}
			uni.request({
				url:uni.getStorageSync('dd')+ 'employee/myId',
				data: {
					"id": uni.getStorageSync('global_ID')
				},
				method: 'POST',
				heads: {
					'content-type': 'application/x-www-form-urlencoded'
				},
				header: {
					"token": uni.getStorageSync('token')
				},
				success: (res) => {
					console.log(res.data);
					if (res.data.code == 200) {
						this.form = res.data.data;
						this.address = this.form.address;
						this.postCode = this.form.postCode;
						this.tel = this.form.tel;
						this.QQNumber = this.form.QQNumber;
						this.email = this.form.email;
						this.hobby = this.form.hobby;
						this.remark = this.form.remark;
						if (this.form.sex == "2") {
							this.sex = '女';
						} else {
							this.sex = '男';
						}
					} else {
						this.showToast(res.data.message);
					}
				}
			})
		},
		methods: {
			change() {
				console.log('change');
				uni.request({
					url: uni.getStorageSync('dd')+'employee/change',
					data: {
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
						"sex": this.form.sex,
						"party": this.form.party,
						"birthday": this.form.birthday,
						"race": this.form.race,

						"education": this.form.education,
						"speciality": this.form.speciality,
						"hobby": this.form.hobby,
						"remark": this.form.remark,
						"createDate": this.form.createDate,
						"status":this.form.status
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
							this.showToast(res.data.message);
						}
					}
				})
			},
			save_address() {
				this.form.address = this.address;
				console.log(this.form.address);
				this.show_address = false;
				this.change();
			},
			save_postCode() {
				this.form.postCode = this.postCode;
				console.log(this.form.postCode);
				this.show_postCode = false;
				this.change();
			},
			save_tel() {
				this.form.tel = this.tel;
				console.log(this.form.tel);
				this.show_tel = false;
				this.change();
			},
			save_QQNumber(){
				this.form.QQNumber = this.QQNumber;
				console.log(this.form.QQNumber);
				this.show_QQNumber = false;
				this.change();
			},
			save_email(){
				this.form.email = this.email;
				console.log(this.form.email);
				this.show_email = false;
				this.change();
			},
			save_hobby(){
				this.form.hobby = this.hobby;
				console.log(this.form.hobby);
				this.show_hobby = false;
				this.change();
			},
			save_remark(){
				this.form.remark = this.remark;
				console.log(this.form.remark);
				this.show_remark = false;
				this.change();
			},
			click_address() {
				console.log("click address");
				this.show_address = true;
			},
			click_postCode() {
				console.log("click postCode");
				this.show_postCode = true;
			},
			click_tel() {
				console.log("click tel");
				this.show_tel = true;
			},
			click_QQNumber() {
				console.log("click QQNumber");
				this.show_QQNumber = true;
			},
			click_email() {
				console.log("click email");
				this.show_email = true;
			},
			click_hobby() {
				console.log("click hobby");
				this.show_hobby = true;
			},
			click_remark() {
				console.log("click remark");
				this.show_remark = true;
			},
			showToast(Msg) {
				this.$refs.uToast.show({
					title:Msg,
					type: 'error'
				})
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
