<template>
	<view>		
		<view class="secName">
			<view class="inputLabel"> 
				<text style="font-size: 20px;font-weight: bold;margin-left: 20px;">职位名称</text>
			</view>
			<view class="inputName">
				<view style="padding-top: 5px;text-align: center;">
					<text class="inputText">{{name}}</text>
				</view>
			</view>
		</view>
		<view class="input">
			<image src="../../static/pink.png" class="startd" mode="aspectFill" ></image>
			<view class="infotext">
				<text style="font-weight: bold;font-size: 16px;">职位详细信息</text>
			</view>
		</view>
		<view class="inputArea">
			<view style="padding:20px;">
				<text style="font-size: 16px;">{{intro}}</text>
			</view>
		</view>
		<!-- <view class="line btnpos">
			<button class="btn" @click="submit">返回</button>
		</view> -->
	</view>
</template>

<script>
	export default {
		data() {
			return {
				name: '',
				intro: ''
			}
		},

		onLoad(){
			uni.getStorage({
				key:'clickPosition',
				success:(res)=>{
					this.name = res.data.jobName;
					this.intro = res.data.jobRemark;
				}
			})
		},
		methods: {
			//返回上个页面
			// submit(){
			// 	uni.navigateTo({
			// 		url:'/pages/position/position'
			// 	})
			// }
		}
	}
</script>

<style>
	page{background-color: #F4E5E8;}
	
	.startd{
		width: 100rpx;
		height: 100rpx;
		margin-left: 20px;
		margin-top: 5px;
	}
	
	.input{
		height: 120rpx;
		width: 100%;
		-moz-box-shadow: 0px 0px 10px #BEBEBE;
		-webkit-box-shadow: 0px 0px 10px #BEBEBE;
		box-shadow: 0px 0px 10px #BEBEBE;
		display: flex;
		margin-top: 30px;
		background-color: #FFFFFF;
	}
	.infotext{
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
		font-size: 20px;
		font-weight: bold;
	}

	.inputArea {
		width: 95%;
		height: 900rpx;
		margin-left: 10px;
		margin-top: 30rpx;
		background-color: #FFFFFF;
		border-radius: 15rpx;
	}
	
	.inputName {
		width: 80%;
		height: 40px;
		margin-top: 15px;
		margin-left: 10%;
		background-color: #f9faf9;
		border-radius: 15rpx;
	}
	
	.inputLabel{
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
	
	.custom-style{
		background-color: #ECE8FB;
	}
	
	.btn{
		margin-top: 10px;
		width:95%;
		background-color: #FFFFFF;
		font-size: 16px;
		font-weight: bold;
	}
</style>
