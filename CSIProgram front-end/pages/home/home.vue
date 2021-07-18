<template>
	<view>
		<view>
			<u-swiper :list="banner_list" mode="rect" :effect3d="true" height="420"></u-swiper>
		</view>

		<view style="display: flex;flex-direction: row;margin-top: 5%;">
			<view style="background-color: #DBFAFF;border-radius: 50px;height:80px;width: 80px;margin-left: 7%;"
				@click="click_employee">
				<image src="/static/employee.png" style="width: 60px;height: 60px;margin-left:12%;margin-top: 10%;">
				</image>
				<view style="margin-top: 15%;">
					<text style="font-size: 15px;font-weight: 700;margin-left:25%;"> 员工</text>
				</view>
			</view>
			<view style="background-color: #F1FFED;border-radius: 50px;height:80px;width: 80px;margin-left: 10%;"
				@click="click_position">
				<image src="/static/position.png" style="width: 60px;height: 60px;margin-left:14%;margin-top: 13%;">
				</image>
				<view style="margin-top: 13%;">
					<text style="font-size: 15px;font-weight: 700;margin-left:28%;"> 职位</text>
				</view>
			</view>

			<view style="background-color: #FFF6EC;border-radius: 50px;height:80px;width: 80px;margin-left: 10%;"
				@click="click_department">
				<image src="/static/department.png" style="width: 60px;height: 55px;margin-left:13%;margin-top: 13%;">
				</image>
				<view style="margin-top: 20%;">
					<text style="font-size: 15px;font-weight: 700;margin-left:28%;"> 部门</text>
				</view>
			</view>
		</view>

		<view style="margin-top: 16%;">
			<u-notice-bar mode="vertical" :list="notice_list" :is-circular=false :duration="5000" color="#A994FB"
				bg-color="#E9E4FE" style="margin-left: 6%;margin-right: 8%;"></u-notice-bar>
		</view>

		<view style="background-color: #FFF8E5;margin-left: 6%;margin-right: 8%;border-radius: 10px;margin-top: 8%;"
			@click="click_list0">

			<view style="padding-top: 5%;padding-left: 3%;padding-right: 3%;">
				<text style="font-size: 15px;font-weight: bold;">{{this.list[0].title}}</text>
			</view>


			<view style="display: flex;flex-direction: row-reverse;padding-top: 5%;">
				<text style="padding-right: 3%;">{{this.list[0].createDate}}</text>
				<image src="/static/date.png" style="width: 15px;height:15px;padding-right: 2%;"></image>
			</view>
			
		</view>
		
		
		<view style="background-color: #ECFDFF;margin-left: 6%;margin-right: 8%;border-radius: 10px;margin-top: 8%;"
			@click="click_list1">
		
			<view style="padding-top: 5%;padding-left: 3%;padding-right: 3%;">
				<text style="font-size: 15px;font-weight: bold;">{{this.list[1].title}}</text>
			</view>
		
		
			<view style="display: flex;flex-direction: row-reverse;padding-top: 5%;">
				<text style="padding-right: 3%;">{{this.list[1].createDate}}</text>
				<image src="/static/date.png" style="width: 15px;height:15px;padding-right: 2%;"></image>
			</view>
			
		</view>
		
		<view>
			<u-toast ref="uToast" />
		</view>
	</view>
</template>

<script>
	import helper from '../../common/base.js'
	export default {
		data() {
			return {
				list: [{
					title: '',
					createDate: ''
				}, {
					title: '',
					createDate: ''
				}],
				notice_list: [
					'超越自己，超越梦想',
					'精神成就事业，态度决定一切',
					'越努力越幸福',
					'机会是留给有准备的人'
				],
				banner_list: [{
						image: '/static/t1.jpg'
					},
					{
						image: '/static/t2.jpg'
					},
					{
						image: '/static/t3.jpg'
					}
				]
			}
		},
		onLoad(){
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
			
			uni.request({
				url: helper.websiteUrl+'/department/getAll',
				data: {},
				method: 'GET',
				header: {
					"token": uni.getStorageSync('token')
				},
				success: (res) => {
					if (res.data.code == 200) {
						uni.setStorageSync('global_department_list',res.data.data);
					} else {
						this.$refs.uToast.show({
							title: '获取部门信息失败',
							type: 'error'
						})
					}
				}
			});
			
			
			uni.request({
				url: helper.websiteUrl+'/job/getAll',
				data: {},
				method: 'GET',
				header: {
					"token": uni.getStorageSync('token')
				},
				success: (res) => {
					if (res.data.code == 200) {
						uni.setStorageSync('global_job_list',res.data.data);
					} else {
						this.$refs.uToast.show({
							title: '获取职位信息失败',
							type: 'error'
						})
					}
				}
			});
			uni.request({
				url: helper.websiteUrl+'/announcement/getAll',
				data: {},
				method: 'GET',
				header: {
					"token": uni.getStorageSync('token')
				},
				success: (res) => {
					if (res.data.code == 200) {
						uni.setStorageSync('global_announcement_list',res.data.data);
					} else {
						this.$refs.uToast.show({
							title: '获取公告信息失败',
							type: 'error'
						})
					}
				}
			});
			//获得已读列表
			uni.request({
				url: helper.websiteUrl +
					'/announcement/searchAnnouncementWithEmployee', //链接地址http://p40974t583.qicp.vip/announcement/getAll
				data: {
					"id": this.id,
					"password": "str",
					"departmentName": "str",
					"departmentRemark": "str",
					"jobName": "str",
					"jobRemark": "str",
					"name": "str",
					"cardId": "str",
					"address": "str",
					"postCode": "str",
					"tel": "str",
					"phone": "str",
					"QQNumber": "str",
					"email": "str",
					"sex": "str",
					"party": "str",
					"birthday": "str",
					"race": "str",
					"education": "str",
					"speciality": "str",
					"hobby": "str",
					"remark": "str",
					"createDate": "str",
					"status": "str"
				},
				dataType: 'json',
				method: 'POST',
				header: {
					"token": uni.getStorageSync('token')
				},
				success: res => {
					console.log(res.data);
					if (res.data.code == 200) {
			uni.setStorageSync('global_read_list',res.data.data);
			
			
					}
				}
			});
			//获得未读列表
			uni.request({
				url: helper.websiteUrl +
					'/announcement/searchUnreadAnnouncementWithEmployee', //链接地址http://p40974t583.qicp.vip/announcement/getAll
				data: {
					"id": this.id,
					"password": "str",
					"departmentName": "str",
					"departmentRemark": "str",
					"jobName": "str",
					"jobRemark": "str",
					"name": "str",
					"cardId": "str",
					"address": "str",
					"postCode": "str",
					"tel": "str",
					"phone": "str",
					"QQNumber": "str",
					"email": "str",
					"sex": "str",
					"party": "str",
					"birthday": "str",
					"race": "str",
					"education": "str",
					"speciality": "str",
					"hobby": "str",
					"remark": "str",
					"createDate": "str",
					"status": "str"
				},
				dataType: 'json',  
				method: 'POST',
				header: {
					"token": uni.getStorageSync('token')
				},
				success: res => {
					console.log(res.data);
					if (res.data.code == 200) {
			uni.setStorageSync('global_unread_list',res.data.data);
	console.log(uni.getStorageSync('global_unread_list'));
					}	
				}
			});
		},
		onShow() {
			uni.request({
				url: helper.websiteUrl+'/announcement/getAll',
				data: {},
				method: 'GET',
				header: {
					"token": uni.getStorageSync('token')
				},
				success: (res) => {
					if (res.data.code == 200) {
						uni.setStorageSync('global_announcement_list',res.data.data);
					} else {
						this.$refs.uToast.show({
							title: '获取公告信息失败',
							type: 'error'
						})
					}
				}
			});
			//获得公告列表
			console.log('主页on show');
			uni.request({
				url: helper.websiteUrl + '/announcement/getAll', //链接地址http://p40974t583.qicp.vip/announcement/getAll
				data: {},
				dataType: 'json',
				method: 'GET',
				header: {
					"token": uni.getStorageSync('token')
				},
				success: res => {
					console.log(res.data);
					if (res.data.code == 200) {
						console.log(res.data.data);
						this.list = res.data.data;
						if(this.list.length==0){
							this.list[0]={};
							this.list[1]={};
						}else if(this.list.length==1){
							this.list[1]={};
						}else{
							this.list = res.data.data;
						}
					}
				}
			});
		},
		methods: {

			click_list0() {
				console.log('click list0');
				uni.setStorage({
					key: 'announcementTitle',
					data: this.list[0].title,

					success: (res) => {
						console.log("存入公告title成功")
					}

				});
				uni.navigateTo({
					url: '../announcementDetail/announcementDetail'
				});

			},
			click_list1() {
				console.log('click list1');
				uni.setStorage({
					key: 'announcementTitle',
					data: this.list[1].title,

					success: (res) => {
						console.log("存入公告title成功")
					}

				});
				uni.navigateTo({
					url: '../announcementDetail/announcementDetail'
				});
			},
			click_notice() {
				console.log('click notice');
			},
			getMore() {

			},
			click_employee() {
				console.log('click employee');
				uni.navigateTo({
					url: '../employee/employee'
				})
			},
			click_position() {
				console.log('click position');
				uni.navigateTo({
					url: '../position/position'
				})
			},
			click_department() {
				console.log('click department');
				uni.navigateTo({
					url: '../department/department'
				})
			}

		}
	}
</script>

<style>

</style>
