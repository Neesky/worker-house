<template>
	<view class="content">
    
		<u-card class="card"    :body-border-bottom="false">
			<view slot="head">
				<text  class="flex flex-direction" style="font-size: 50rpx;color: #000000;">{{topTitle}}\n</text>
			<text  class="flex flex-direction" style="font-size: 30;color: #9d9d9d;">{{subTitle}}</text>	
			</view>
			<view class="" slot="body">
				<view class="u-body-item u-flex u-border-bottom u-col-between u-p-t-0">
					<view class="u-body-item-title ">{{mainBody}}</view>
					<!-- 					<image
						src="https://img11.360buyimg.com/n7/jfs/t1/94448/29/2734/524808/5dd4cc16E990dfb6b/59c256f85a8c3757.jpg"
						mode="aspectFill"></image> -->
				</view>

			</view>
			<view class="foot" slot="foot">
				<text>发布者：{{publisher}}</text>
				<view v-if="viewAble">
					<u-icon name="eye" size="34" color="" label=""></u-icon>已读
					<view class="viewList" v-for="(item,index) in viewList">
						{{item.name}}
					</view>
				</view>
			</view>
		</u-card>

	</view>
</template>

<script>
	import helper from '../../common/base.js'
	export default {
		data() {
			return {
				id: uni.getStorageSync('global_ID'),
				topTitle: '',
				subTitle: '',
				mainBody: '',
				publisher: '',
				viewList: [],
				status: uni.getStorageSync('global_status'),
				viewAble: false
			};
		},
		//获得上个页面的文章名称和文章详情
		onShow() {
			if (uni.getStorageSync('global_status') == '1'){ 
				this.viewAble = true;}
			this.topTitle = uni.getStorageSync('announcementTitle');

			console.log(this.topTitle);
			console.log(uni.getStorageSync('global_ID'));
			//向后端发送请求，id，得到公告详情
			uni.request({ //http://p40974t583.qicp.vip/announcement/appendEmployeeWithAnnouncement
				url: helper.websiteUrl + '/announcement/appendEmployeeWithAnnouncement', //链接地址
				data: {
					"id": uni.getStorageSync('global_ID'),
					"title": this.topTitle
				},
				dataType: 'json',
				method: 'POST',
				header: {
					"token": uni.getStorageSync('token')
				},
				success: res => {
					console.log(res.data);
					if (res.data.code == 200) {
						console.log("连接成功");
						this.topTitle = res.data.data[0].title;
						this.subTitle = res.data.data[0].createDate;
						this.mainBody = res.data.data[0].content;
						this.publisher = res.data.data[0].initiatorName;
						console.log(this.topTitle);
						console.log(this.subTitle);
						//更新已读未读
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
						
									}
							}
						});
					
					}
				}
			});
			//获得阅读过公告的人员名单
			uni.request({ //http://p40974t583.qicp.vip/announcement/searchEmployeeWithAnnouncement
				url: helper.websiteUrl + '/announcement/searchEmployeeWithAnnouncement', //链接地址
				data: {
					"title": this.topTitle,
					"createDate": this.subTitle,
					"content": this.mainBody,
					"initiatorName": this.publisher

				},
				dataType: 'json',
				method: 'POST',
				header: {
					"token": uni.getStorageSync('token')
				},
				success: res => {
					console.log(res.data);
					if (res.data.code == 200) {

						//this.dataSet(res.data.data);
						//console.log(res.data.Data.length);
						this.viewList = res.data.data;
						// console.log("this.viewList"+this.viewList);
						// console.log("this.topTitle"+this.topTitle);
						// console.log("this.subTitle"+this.subTitle);
						// console.log("this.mainBody"+this.mainBody);
						// console.log("this.publisher"+this.publisher);



					}
				}
			});



			// uni.getStorage({
			// 	key: 'announcementTitle',
			// 	success: (res)=> {
			// 	console.log("取出的：");
			// 	console.log(res.data);
			// 	console.log(this.topTitle);
			// 		this.topTitle = res.data[0].title;
			// 		this.subTitle = res.data[0].createDate;
			// 		this.mainBody = res.data[0].content;
			// 		this.publisher = res.data[0].initiatorName;

			// 		console.log(this.topTitle);



			//	this.$forceUpdate();
		},
		methods: {


		}
	};
</script>

<style scoped lang="scss">
	.u-card-wrap {
		background-color: $u-bg-color;
		padding: 1px;
	}

	.u-body-item {
		font-size: 32rpx;
		color: #333;
		padding: 20rpx 10rpx;
	}

	.u-body-item image {
		width: 120rpx;
		flex: 0 0 120rpx;
		height: 120rpx;
		border-radius: 8rpx;
		margin-left: 12rpx;

	}
</style>
<style>
	page {
		background-color: #d2eae0;
	}

	.card {

		height: 1400rpx;

	}

	.foot {
		margin-bottom: 200rpx;
	}
</style>
