<template>
	<view class="content">
		<view class="login">
			<image class="logo" model="widthFix" src="/static/login_avatar.png"></image>
			<text style="font-size:24px">{{text}}</text>
		</view>
		<form name="from1">
			<!--账号-->
			<view class="inputView">
				<image class="nameImage" src="/static/login_id.png"></image>

				<input class="inputText" type="text" placeholder="请输入ID" value="user" v-model="id" border="true"
					placeholder-style='color:rgb(126, 126, 126);font-size:34rpx;' />
			</view>
		</form>
		<!--</ad>  <view class="line"></view>-->
		<!--密码-->
		<view class="inputView">
			<image class="keyImage" src="/static/login_pw.png"></image>

			<input class="inputText" password="true" type="text" placeholder="请输入密码" value="pass" v-model="passw"
				placeholder-style='color:rgb(126, 126, 126);font-size:34rpx;' />
		</view>
		<!-- 记住密码 -->

		<view style="display: flex;flex-direction: row;margin-left: 18%;">
			<view class=" mui-input-row mui-checkbox ">
				<checkbox-group @change="checkboxChange">
					<checkbox id="chkRem" type="checkbox" :checked="rememberPsw" @tap="rememberPsw = !rememberPsw"
						class="RememberCheck">
						记住密码
					</checkbox>
				</checkbox-group>
			</view>
			<text style="color: #9EC2EC;margin-left: 33%;margin-top: 4%;" @click="forget_password">忘记密码？</text>
		</view>


		<!--按钮-->
		<view class="loginBtnView"><button class="loginBtn" @tap="lands">{{btn_text}}</button></view>

		<!--背景图-->
		<!--  <image class="backlogo" src="../../static/BGNew.png"></image>-->
		<view>
			<u-toast ref="uToast" />
		</view>

		<u-modal v-model="show_modal" :show-confirm-button=true content="请携带有效身份证件,前往管理员处修改密码" :show-title=false>
		</u-modal>
	</view>
</template>

<script>
	export default {
		data() {

			return {
				title: '标题',
				id: '',
				passw: '',
				rememberPsw: true,
				text: '员工之家',
				token: '',
				show_modal: false,
				btn_text: '登录'
			};
		},
		//页面初始加载
		mounted() {
			uni.setStorageSync('dd', '填写服务器ip及其端口号');
			
			console.log(uni.getStorageSync('global_password') + "缓存的密码");
			console.log(uni.getStorageSync('global_ID') + "缓存的账号");
			//有缓存就赋值给文本没有就清空
			if (uni.getStorageSync('global_ID') && uni.getStorageSync('global_password')) {
				
				
				this.id = uni.getStorageSync('global_ID');
				this.passw = uni.getStorageSync('global_password');
				
				uni.request({
					url: uni.getStorageSync('dd') + 'login/', //链接地址
					data: {
						"id": this.id,
						"password": this.passw,
						"oaid": uni.getStorageSync('global_oaid')
					},
					dataType: 'json',
					method: 'POST',
					success: res => {
						console.log(res.data);
						this.showToast(res.data.message, 'success');
						//成功
						if (res.data.code == 200) {
							this.token = res.data.data[1];
							console.log("token:" + this.token);
							uni.setStorageSync('token', this.token);
							//登录成功后将id,身份存入本地
							this.btn_text = '正在登陆';
							uni.switchTab({
								url: '../home/home'
							})
							uni.setStorageSync('global_ID', this.id);
							uni.setStorageSync('global_status', res.data.data[0]);
							console.log(uni.getStorageSync('global_status'));
							//缓存账号和密码
							if (this.rememberPsw) {
								uni.setStorageSync('global_password', this.passw);
							} else {
								uni.removeStorageSync('global_password');
							}
				
							uni.switchTab({
								url: '/pages/home/home'
							})
						} else {
							if(res.data.data[2]>5){
								this.showToast("账号已锁定，请稍后尝试", 'error');
							}else{
								if(res.data.message=="登录超限，请在1分钟后尝试"){
									this.showToast("账号已锁定，请在1分钟后尝试", 'error');
								}else{
									if(res.data.data[2]>0){
										this.showToast(res.data.message+"，剩余"+(6-res.data.data[2])+"次机会", 'error');
									}else{
										this.showToast(res.data.message, 'error');
									}
									
								}
							}
						}
					}
				});
				
			} else {
				this.id = '';
				this.passw = '';
			}
		},
		onShow(){
			//#ifdef APP-PLUS
			plus.device.getOAID({
				success: function(e) {
					uni.setStorageSync('global_oaid',JSON.parse(JSON.stringify(e))['oaid']);
					console.log(uni.getStorageSync('global_oaid'));
				}
			})
			//#endif
		},
		methods: {
			forget_password() {
				this.show_modal = true;
			},
			showToast(Msg, Type) {
				this.$refs.uToast.show({
					title: Msg,
					type: Type
				})
			},
			//登陆
			lands() {
				uni.setStorageSync('dd', 'http://47.108.143.150:23451/');

				if (this.id.length <= 0 || this.passw.length <= 0) {
					this.showToast('账号或密码不能为空', 'warning');
					return;
				} else {
					//登录
					
					uni.request({
						url: uni.getStorageSync('dd') + 'login/', //链接地址
						data: {
							"id": this.id,
							"password": this.passw,
							"oaid": uni.getStorageSync('global_oaid')
						},
						dataType: 'json',
						method: 'POST',
						success: res => {
							console.log(res.data);
							this.showToast(res.data.message, 'success');
							//成功
							if (res.data.code == 200) {
								this.token = res.data.data[1];
								console.log("token:" + this.token);
								uni.setStorageSync('token', this.token);
								//登录成功后将id,身份存入本地
								uni.setStorageSync('global_ID', this.id);
								uni.setStorageSync('global_status', res.data.data[0]);
								console.log(uni.getStorageSync('global_status'));
								//缓存账号和密码
								if (this.rememberPsw) {
									uni.setStorageSync('global_password', this.passw);
								} else {
									uni.removeStorageSync('global_password');
								}

								uni.switchTab({
									url: '/pages/home/home'
								})
							} else {
								if(res.data.data[2]>5){
									this.showToast("账号已锁定，请稍后尝试", 'error');
								}else{
									if(res.data.message=="登录超限，请在1分钟后尝试"){
										this.showToast("账号已锁定，请在1分钟后尝试", 'error');
									}else{
										if(res.data.data[2]>0){
											this.showToast(res.data.message+"，剩余"+(6-res.data.data[2])+"次机会", 'error');
										}else{
											this.showToast(res.data.message, 'error');
										}
										
									}
								}
							}
						}
					});
					//else
				}


			},

			//复选框
			checkboxChange: function(e) {

				console.log(e.detail.value.length);
				if (e.detail.value.length == 1) {
					//获取缓存的账号
					uni.getStorageSync('global_ID', this.id);
					uni.getStorageSync('global_password', this.passw);
				} else {
					uni.removeStorageSync('global_password');
				}
			}
		}
	};
</script>

<style>
	.login {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}

	.logo {
		height: 300rpx;
		width: 300rpx;
		margin-top: 100rpx;
		margin-left: auto;
		margin-right: auto;
		margin-bottom: 50rpx;
	}

	.mui-checkbox input[type='checkbox']:checked:before {
		color: #00bbb1;
	}

	.RememberPass {
		color: #adadad;

		margin-top: 5px;
	}

	.RememberCheck {
		margin-left: -50%;
		margin-top: 10px;
		color: #adadad;
	}

	.content {
		text-align: center;
		height: 400upx;
	}


	.title {
		/* font-size: 36upx; */
		color: mediumaquamarine;
		font-size: 150%;
	}

	.text {
		border: 1, solid, black;
	}

	.login-from {
		margin-top: 30%;

		flex: auto;
		height: 100%;
		width: 100%;
	}

	.inputView {

		margin: 40rpx;
		border-radius: 25rpx;
		/*	border: 6rpx solid #9EC2EC;*/

		background-color: #efefef;
		line-height: 95rpx;
		border-width: 4px;
		border-bottom: 2dp;


	}

	/*输入框*/
	.nameImage,
	.keyImage {
		margin-left: 15rpx;
		margin-button: 3rpx;
		margin-top: 25rpx;
		width: 50rpx;
		height: 50rpx;
	}

	.inputText {
		width: 500rpx;
		border-radius: true;
		background-color: #efefef;
	}

	.loginLab {
		margin: 15px 15px 15px 10px;
		color: #f9faf9;
		font-size: 18px;
	}

	.inputText {
		flex: block;
		float: right;
		text-align: left;
		margin-right: 22px;
		margin-top: 15px;
		color: #0c0c0c;
		font-size: 18px;
		height: 100%;
	}

	.line {
		width: 100%;
		height: 1px;
		background-color: #ffffff;
		margin-top: 1px;
	}

	/*按钮*/
	.loginBtnView {
		width: 100%;
		height: auto;
		/* background-color:#FFFFFF; */
		margin-top: 50px;
		margin-bottom: 0px;
		padding-bottom: 0px;
	}

	.loginBtn {
		width: 90%;
		margin-top: 50px;
		background-color: #9EC2EC;
		color: aliceblue;
	}
</style>
