<template>
	<view>
		<view>
			<u-toast ref="uToast" />
		</view>
		
		<!-- 修改职位名称 -->
		<view class="secName">
			<view class="inputLabel"> 
				<text style="font-size: 20px;font-weight: bold;margin-left: 20px;">请修改职位名称</text>
			</view>
			<input class="inputText" v-model="name" />
		</view>
		
		<!-- 职位详细信息 -->
		<view class="input">
			<image src="../../static/pink.png" class="startd" mode="aspectFill" ></image>
			<view class="infotext">
				<text style="font-weight: bold;font-size: 16px;">请修改职位详细信息</text>
			</view>
		</view>
		<!-- 输入框 -->
		<view class="inputArea">
			<textarea v-model="intro" style="padding:20px;" />
		</view>
		
		<!-- 修改按钮 -->
		<view class="line btnpos">
			<button class="btn" @click="submit">修改</button>
		</view>
	</view>
</template>

<script>
	import helper from '../../common/base.js'
	export default {
		data() {
			return {
				name: '',
				intro: '',
				joboldname:''
			}
		},

		onLoad(){
			//取出缓存中职位的相关信息
			uni.getStorage({
				key:'clickPositionbox',
				success:(res)=>{ 
					this.name = res.data.jobName;  //职位名称
					this.joboldname = res.data.jobName;  //职位旧名称
					this.intro = res.data.jobRemark;  //职位详情
				}
			})
		},
		methods: {
			submit(){
				//名称和详情不能为空
				if (this.name && this.intro) {
					console.log("hello");
					console.log(this.name);
					console.log(this.intro);
					uni.request({
						url: helper.websiteUrl+'/job/change', //链接地址
						data: {  //传过去职位新旧名称和详情
							"jobNewName":this.name,
							"jobName": this.joboldname,
							"jobRemark": this.intro
						},
						header: {
							"token": uni.getStorageSync('token')
						},
						dataType: 'json',
						method: 'POST',
						success: (res) => {
							if (res.data.code == 200){	//修改成功
								this.$refs.uToast.show({
									title: '修改职位成功',
									type: 'success',
									duration:600
								})
								
								
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
							else{
								this.$refs.uToast.show({ //修改失败
									title: '修改职位失败',
									type: 'error',
									back:true,
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
	
	/* 图片位置及大小 */
	.startd{
		width: 100rpx;
		height: 100rpx;
		margin-left: 20px;
		margin-top: 5px;
	}
	
	/* 部门详细信息 */
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
	
	/* 部门名称 */
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
	
	/* 输入框 */
	.inputArea {
		width: 95%;
		height: 800rpx;
		margin-left: 10px;
		margin-top: 30rpx;
		background-color: #FFFFFF;
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
	
	/* 按钮 */
	.line {
		display: flex;
		flex-direction: row;
	}

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
