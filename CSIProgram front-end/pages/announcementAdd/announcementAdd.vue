<template>
	<view>
		<view>
			<u-toast ref="uToast" />
		</view>
		
		<view class="secName">
			<view class="inputLabel">
				<text style="font-size: 20px;font-weight: bold;margin-left: 20px;">标题</text>
			</view>
			<input class="inputText" placeholder="请填写标题" v-model="title" />
		</view>
		<view class="input">
			<!--<image src="../../static/purple.png" class="startd" mode="aspectFill" ></image>-->
			<view class="infotext">
				<text style="font-weight: bold;font-size: 16px;">正文</text>
				
			</view>
		</view>
		<view class="inputArea">
			<textarea v-model="intro" style="padding:20px;" placeholder="请填写正文" />
		</view>

		<view class="secPublisher">
			<view class="inputLabel">
				<text style="font-size: 20px;font-weight: bold;margin-left: 20px;">发布者</text>
			</view>
			<input class="inputText" placeholder="请填写发布者姓名或组织机构名称" v-model="publisher" />
		</view>
		<view class="line btnpos">
			<button class="btn" @click="submit">提交</button>
		</view>
	</view>
</template>

<script>
	import helper from '../../common/base.js'
	import currentDate from ' ../..//common/util/currentDate.js';
	export default {
		data() {
			return {
				title: '',
				intro: '',
				publisher: '',
				date: currentDate.getDate(),
			}
		},
		onload() {
			console.log(this.date);
		},
		methods: {
			//发送数据 返回上个页面
			submit() {

				if (this.title && this.intro && this.publisher) {

					uni.request({
						url: helper.websiteUrl + '/announcement/append', //链接地址
						data: {
							"title": this.title,
							"initiatorName": this.publisher,
							"createDate": this.date,
							"content": this.intro
						},
						header: {
							"token": uni.getStorageSync('token')
						},
						dataType: 'json',
						method: 'POST',
						success: (res) => {
							if (res.data.code == 200) {
								console.log("提交");
								//获得公告列表
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
										setTimeout(()=>{
											uni.switchTab({ //uni.navigateTo跳转的返回，默认1为返回上一级
												 url: '../tool/tool'
											});
										},200);
									}
								});
								
							} else {
							
								this.$refs.uToast.show({
									title: res.data.message,
									type: 'error'
								}) 
							}
						}
					});
					
				} else {
					this.$refs.uToast.show({
						title: '内容不为空',
						type: 'error'
					})
				}
			}
		}
	}
</script>

<style>
	page {
		background-color: #ECE8FB;
	}

	.startd {
		width: 100rpx;
		height: 100rpx;
		margin-left: 20px;
		margin-top: 5px;
	}

	.input {
		height: 120rpx;
		width: 100%;
		-moz-box-shadow: 0px 0px 10px #BEBEBE;
		-webkit-box-shadow: 0px 0px 10px #BEBEBE;
		box-shadow: 0px 0px 10px #BEBEBE;
		display: flex;
		margin-top: 20px;
		background-color: #FFFFFF;
	}

	.secPublisher {
		margin-top: 20px;
		border-radius: 10rpx;
		height: 220rpx;
		width: 95%;
		margin-left: 8px;
		/* 加阴影*/
		-moz-box-shadow: 0px 0px 10px #BEBEBE;
		-webkit-box-shadow: 0px 0px 10px #BEBEBE;
		box-shadow: 0px 0px 10px #BEBEBE;
		background-color: #FFFFFF;
	}

	.infotext {
		margin-top: 14px;
		margin-left: 10px;
	}

	.secName {
		border-radius: 10rpx;
		height: 220rpx;
		width: 95%;
		margin-left: 8px;
		/* 加阴影*/
		-moz-box-shadow: 0px 0px 10px #BEBEBE;
		-webkit-box-shadow: 0px 0px 10px #BEBEBE;
		box-shadow: 0px 0px 10px #BEBEBE;
		background-color: #FFFFFF;
	}

	.inputText {
		margin-top: 15px;
		margin-left: 10%;
		margin-bottom: 10%;
		height: 30px;
		width: 80%;
		background-color: #f9faf9;
		border-radius: 15rpx;
	}

	.inputArea {
		width: 95%;
		height: 800rpx;
		margin-left: 10px;
		margin-top: 30rpx;
		background-color: #FFFFFF;
		border-radius: 15rpx;
	}

	.inputLabel {
		padding-top: 10px;
	}

	.secIntro {
		border-radius: 15rpx;
		margin-top: 60rpx;
		background-color: #f5e7dd;
		width: 100%;
		height: 1000rpx;
		/* 加阴影*/
		-moz-box-shadow: 2px 2px 10px #f5f4f4;
		-webkit-box-shadow: 2px 2px 10px #f5f4f4;
		box-shadow: 2px 2px 10px #f5f4f4;
	}

	.line {
		display: flex;
		flex-direction: row;
	}

	.btnpos {
		display: flex;
		margin-top: 10px;
	}

	.custom-style {
		background-color: #ECE8FB;
	}

	.btn {
		margin-top: 10px;
		width: 95%;
		background-color: #FFFFFF;
		font-size: 16px;
		font-weight: bold;
	}
</style>
