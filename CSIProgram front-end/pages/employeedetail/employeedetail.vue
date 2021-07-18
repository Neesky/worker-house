<template>
	<view>
		<view>
			<u-toast ref="uToast" />
		</view>
		
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

			<u-form-item label="部门信息" style="font-size:16px;" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<text style="color: #BBBBBB;font-size: 16px;"> {{form.departmentRemark}}</text>
				</view>
			</u-form-item>

			<u-form-item label="职位" style="font-size:16px;" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<text style="color: #BBBBBB;font-size: 16px;"> {{form.jobName}}</text>
				</view>
			</u-form-item>

			<u-form-item label="职位信息" style="font-size:16px;" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<text style="color: #BBBBBB;font-size: 16px;"> {{form.jobRemark}}</text>
				</view>
			</u-form-item>
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
		<u-gap height="30" bg-color="#f3f4f6"></u-gap>

		<u-form style="margin-left:10px;" :model="form" ref="uForm">
			<u-form-item label="创建时间" style="font-size:16px;" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<text style="color: #BBBBBB;font-size: 16px;"> {{form.createDate}}</text>
				</view>
			</u-form-item>
		</u-form>
		
		<u-form style="margin-left:10px;" :model="form" ref="uForm">
			<u-form-item label="用户状态" style="font-size:16px;" label-width="80px">
				<view style="width:530rpx;display: flex;flex-direction: row-reverse;">
					<text style="color: #BBBBBB;font-size: 16px;"> {{status}}</text>
				</view>
			</u-form-item>
		</u-form>
		
	</view>
</template>

<script>
	import helper from '../../common/base.js'
	export default {
		data() {
			return {
				form: {},
				id:'',
				sex:'',
				status:''
			}
		},
		onShow() {
			uni.request({
				url: helper.websiteUrl+'/employee/myId',
				data: {
					"id": uni.getStorageSync('employeeId')
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
						if (this.form.sex == "2") {
							this.sex = '女';
						} else {
							this.sex = '男';
						}
						if (this.form.status == "1") {
							this.status = '管理员';
						} else {
							this.status = '普通用户';
						}
					} else {
						this.$refs.uToast.show({
							title: '获取个人信息失败',
							type: 'error'
						})
					}
				}
			});
		},
		methods: {
			
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
