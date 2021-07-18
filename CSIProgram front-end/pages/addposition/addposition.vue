<template>
	<view>
		<view>
			<u-toast ref="uToast" />
		</view>
		
		<!-- 输入职位名称 -->
		<view class="secName">
			<view class="inputLabel"> 
				<text style="font-size: 20px;font-weight: bold;margin-left: 20px;">请输入职位名称</text>
			</view>
			<input class="inputText" placeholder="新建职位名称" v-model="name" />
		</view>
		
		<!-- 输入职位详细信息 -->
		<view class="input">
			<image src="../../static/pink.png" class="startd" mode="aspectFill" ></image>
			<view class="infotext">
				<text style="font-weight: bold;font-size: 16px;">请输入职位详细信息</text>
			</view>
		</view>
		<!-- 输入框 -->
		<view class="inputArea">
			<textarea v-model="intro" style="padding:20px;" />
		</view>
		
		<!-- 提交按钮 -->
		<view class="line btnpos">
			<button class="btn" @click="submit">提交</button>
		</view>
	</view>
</template>

<script>
	import helper from '../../common/base.js'
	export default {
		data() {
			return {
				name: '',
				intro: ''
			}
		},
		
		methods: {
			//名称和详细信息必填
			submit(){
				if (this.name && this.intro) {
					uni.request({
						url: helper.websiteUrl+ '/job/append', //链接地址
						data: {
							"jobName": this.name,
							"jobRemark": this.intro
						},
						dataType: 'json',
						method: 'POST',
						header: {
							"token": uni.getStorageSync('token')  //头部信息中包含token
						},
						success: (res) => {
							if (res.data.code == 200){  //增加职位成功
								this.$refs.uToast.show({
									title: '增加职位成功',
									type: 'success',
									duration:600
								})
								console.log('增加职位成功');
								
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
								
							}
							else{  //增加部门失败
								this.$refs.uToast.show({
									title: '增加职位失败',
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
				else{  //内容为空提示
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
	page{background-color: #F4E5E8;}
	
	/* 图片格式 */
	.startd{
		width: 100rpx;
		height: 100rpx;
		margin-left: 20px;
		margin-top: 5px;
	}
	
	/* 输入部门详细信息 */
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
	
	/* 输入部门名称卡片设置 */
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
	
	.inputLabel{
		padding-top: 10px;
	}
	
	/* 输入框 */
	.inputArea {
		width: 95%;
		height: 800rpx;
		margin-left: 10px;
		margin-top: 30rpx;
		background-color: #FFFFFF;
		border-radius: 15rpx;
	}
	
	/* 排列在一行 */
	.line {
		display: flex;
		flex-direction: row;
	}
	
	/* 按钮位置及颜色 */
	.btnpos {
		display: flex;
		margin-top: 10px;
	}
	
	.btn{
		margin-top: 10px;
		width:95%;
		background-color: #FFFFFF;
		font-size: 16px;
		font-weight: bold;
	}
</style>
