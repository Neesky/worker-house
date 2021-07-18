<template>
	<view class="content">
		<view class="inputTextView">
			<text class="old_pw" style="font-size: 24px; font-weight:bold;">请输入旧密码</text>
			<input class="inputtext" v-model="old_pw" @blur="isa" password="true" />
		</view>

		<view class="inputTextView">
			<text class="flex flex-direction" style="font-size: 24px;font-weight:bold"> 请设置新密码\n</text>
			<text class="flex flex-direction" style="font-size: 14px;color: #a8a8a8;">密码长度为8-20个字符，必须包含字母和数字。</text>
			<input class="inputtext" v-model="new_pw_1" password="true" @blur="limit" />
		</view>

		<view class="inputTextView">
			<text class="new_pw" style="font-size: 24px;font-weight:bold"> 请再次确认新密码</text>
			<input class="inputtext" v-model="new_pw_2" password="true" @blur="iss" />
		</view>

		<view>
			<u-button class="btn" @click="addmit" :ripple="true" style="background-color: #d6beff;" :hair-line="false">
				确认</u-button>
		</view>

		<view>
			<u-toast ref="uToast"/>
		</view>
		
		
	</view>
</template>

<script>
	import helper from '../../common/base.js'
	export default {
		data() {
			return {
				old_pw: '', //输入的旧密码
				new_pw_1: '', //输入的新密码
				new_pw_2: '', //再次输入的新密码
				id: uni.getStorageSync('global_ID'), //
				cur_pw: uni.getStorageSync('global_password'), //从上一个页面获得
				isSame: false, //两次输入密码是否相同
				isAdmit: false, //旧密码是否输入正确
				isConform: false
			};
		},
		methods: {
/* 			callback(){
				console.log('dff');
				uni.switchTab({
					url:"./my"
				})
			}, */
			showToast(Msg, Type) {
				this.$refs.uToast.show({
					title: Msg,
					type: Type,
					isTab:true,
					back:true
				})
			},
			//原密码是否输入正确
			isa(e) {
				this.isAdmit = (this.old_pw == uni.getStorageSync('global_password'));
				console.log("原密码是否输入正确: " + this.isAdmit);
			},
			//两次密码是否相同
			iss(e) {
				this.isSame = (this.new_pw_1 == this.new_pw_2);

				console.log("两次密码是否相同: " + this.isSame);
			},

			limit(e) {
				//长度是否符合
				if (this.new_pw_1.length < 8 || this.new_pw_1.length > 20) {
					this.showToast("密码格式错误", 'error');

				}
				let letter = false; //是否有字母
				let number = false; //是否有数字
				for (let i = 0; i < this.new_pw_1.length; i++) {
					if (this.new_pw_1[i] >= "0" && this.new_pw_1[i] <= "9") {
						number = true;
					}
					if (this.new_pw_1[i] >= "A" && this.new_pw_1[i] <= "Z") {
						letter = true;
					}
					if (this.new_pw_1[i] >= "a" && this.new_pw_1[i] <= "z") {
						letter = true;
					}
				}
				if (letter == false || number == false) {
					this.showToast("密码格式错误", 'error');
					this.isConform = false;
				} else {
					this.isConform = true;
				}
			},
			//确认按钮事件
			addmit() {
				console.log(this.isConform);
				if (this.isConform == true) {
					if (this.old_pw != uni.getStorageSync('global_password')) {
						this.showToast("原密码错误", 'error');
					} else {
						if (this.new_pw_1 != this.new_pw_2) {
							this.showToast("两次输入不一致", 'error');
						} else if (this.new_pw_1 == '') {
							this.showToast("新密码不能为空", 'warning');
						} else {
							console.log(this.new_pw_1);
							console.log(this.id);

							uni.setStorageSync('global_password', this.new_pw_1);
							console.log("global_password:" + uni.getStorageSync('global_password'));
							uni.request({
								url: uni.getStorageSync('dd') + 'login/changePassword',
								data: {
									"id": this.id,
									"password": this.new_pw_1
								},
								method: 'POST',
								header: {
									"token": uni.getStorageSync('token')
								},
								success: (res) => {
									console.log(res.data);
									this.showToast(res.data.message, 'default');
								}
							})

						}
					}
				}
			}
		}
	}
</script>

<style>
	.inputTextView {
		margin-top: 60rpx;
		margin: 25px;
	}

	.inputtext {
		padding-left: 6%;
		background-color: #f9faf9;
		margin-top: 20rpx;
		height: 100rpx;
		border-radius: 20rpx;
		margin-right: 15rpx;

	}

	.btn {
		margin-top: 130rpx;
		width: 90%;
		background-color: #d6beff;
	}
</style>
