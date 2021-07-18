<template>
	<view class="content">
		<u-modal v-model="showdelete" :content="contentdelete" @confirm="confirmdelete" :show-cancel-button="true">
		</u-modal>

		<u-tabs class="tab" :list="tarlist" :is-scroll="false" :current="current" @change="change"
			active-color="#FFFFFF" height="100" font-size="50rpx" bar-height="11" bg-color="#d2eae0"></u-tabs>
		<view class="announcement" v-if="current==0">
			<view class="top">
				<!--管理员可见-->
				<view v-if="viewAble">
					<uni-fab class="btnfab" :pattern="pattern2" :popMenu="false" horizontal="right"
						@fabClick="fabClick2">
					</uni-fab>
				</view>

				<!-- 	<u-tabs-swiper ref="tabs" :list="tarlist" :is-scroll="false" active-color="#9EC2EC" :current="current" @change="tabsChange"  inactive-color="#606266" font-size="40rpx" ></u-tabs-swiper>
 -->
			</view>

			<u-line class="u-line" color="#747d7d"></u-line>
			<!--用户可见-->
			<view class="dropdown" v-if="viewUnable">
				<u-dropdown ref="uDropdown" @open="openDrop" @close="closeDrop">
					<u-dropdown-item v-model="value1" title="范围" :options="options1" @change="changeDrop">
					</u-dropdown-item>

				</u-dropdown>
			</view>
			<view class="card">
				<u-swipe-action :index="index" btn-width="150" v-for="(item, index) in list" :key="item.title"
					@click="click2" :options="options2" :disabled="isDelete">
					<view class="item u-border-bottom">
						<u-card class="card-box" margin="40rpx" padding="20" box-shadow="40" border-radius="40px"
							@click="clickbranch(index)" index="indexCard" :border="false" :foot-border-top="false"
							:head-border-bottom="false" :body-border-bottom="false">
							<view class="" slot="body">
								<view class="u-body-item u-flex u-border-bottom u-col-between u-p-t-0">
									<text class="titleLabel"
										style="color: #000000; font-size: 40rpx;">{{item.title}}</text>
								</view>
							</view>
							<view class="time" slot="foot">
								<u-icon name="calendar" size="34" color="#000000" label=""></u-icon>
								<!-- <u-icon name="eye" size="34" margin-left="24rpx"></u-icon>
							<text font-size='40'>浏览量</text> -->
								<text class="dateLabel" style="color: #000000;">{{item.createDate}}</text>
							</view>
							<view class="number" slot="foot"> </view>
						</u-card>
					</view>
				</u-swipe-action>
			</view>
		</view>
		<view class="downloadCenter" v-if="current==1">
			<view v-if="add_able">
				<uni-fab :pattern="pattern" :popMenu=false horizontal="right" @fabClick="fabClick"
					style="margin-bottom: 40%;position: absolute;"></uni-fab>
			</view>

			<view style="height: 125rpx;background-color: #d2eae0;">
				<u-search placeholder="搜索文件" v-model="keyword" style="padding-top: 5%;" @change="search"
					:show-action="false">
				</u-search>
			</view>

			<view v-if="show_progress">
				<progress :percent="percent" show-info stroke-width="10" duration=30></progress>
			</view>

			<view style="background-color: #d2eae0;">
				<u-swipe-action :index="index" v-for="(item, index) in doc_list" :key="item.title" @click="click"
					:options="options">
					<view style="display: flex;flex-direction: row;margin-top: 4%;margin-bottom: 4%;">
						<image :src="image_select(item.title)"
							style="height: 70rpx;width: 70rpx;padding-top: 4%;padding-left: 4%;"></image>
						<view style="display: flex;flex-direction: column;margin-left: 5%;">
							<textarea style="font-size: 35rpx;width:600rpx;" :value=item.title :auto-height="true"
								:disabled="true"></textarea>
							<text style="font-size: 20rpx;padding-top: 5%;">{{"发布者："+item.initiatorName}}</text>
							<text style="font-size: 20rpx;">{{"发布日期："+item.createDate}}</text>
						</view>
					</view>
					<u-gap height="20" bg-color="#d2eae0"></u-gap>
				</u-swipe-action>
			</view>





			<view style="background-color: #d2eae0;">
				<u-swipe-action>
					<view style="display: flex;flex-direction: row;margin-top: 4%;margin-bottom: 4%;">
						<text style="font-size: 35rpx;margin-left: 250rpx;">没有更多内容了</text>
					</view>
					<u-gap height="20" bg-color="#d2eae0"></u-gap>
				</u-swipe-action>
			</view>

			<view>
				<u-toast ref="uToast" />
			</view>


			<u-modal v-model="show1" title="下载成功" @confirm="confirm">
				<textarea :disabled="true" :auto-height="true"
					value="文件已保存至\Android\data\io.dcloud.HBuilder\apps\HBuilder\doc\uniapp_save"
					style="padding-left: 4%;margin-top: 4%;margin-bottom:4%;width: 560rpx;"></textarea>
			</u-modal>

		</view>
	</view>
</template>

<script>
	import helper from '../../common/base.js'
	export default {
		data() {
			return {
				current: 0, //初始页面是公告页面
				tarlist: [{
					name: '公告'
				}, {
					name: '下载中心',

				}],
				//公告页面
				showdelete: false,
				delete_index: '',
				contentdelete: '确认删除此公告？',
				viewAble: false, //管理员可见
				token: '',
				status: uni.getStorageSync('global_status'), //身份
				viewUnable: false, //用户可见
				id: uni.getStorageSync('global_ID'), //id
				value1: 1,
				isDelete: false,
				// titleDrop: this.options1[value1].label,
				options1: [{
						label: '全部',
						value: 1,
					},
					{
						label: '已读',
						value: 2,
					},
					{
						label: '未读',
						value: 3,
					}
				],

				options2: [{
						text: '删除',
						style: {
							backgroundColor: '#dd524d'
						}
					}]

					,
				pattern2: {
					color: 'gray',
					backgroundColor: '#98C080',
					selectedColor: '#98C080',
					buttonColor: '#98C080 '
				},

				list: [],
				indexCard: 0,
				//下载中心页面
				percent: 0,
				show_progress: false,
				show1: false,
				add_able: true,
				pattern: {
					color: 'gray',
					backgroundColor: '#FFFFFF',
					selectedColor: '#98C080',
					buttonColor: '#98C080'
				},
				keyword: '',
				options: [{
						text: '下载',
						style: {
							backgroundColor: '#9EB7EC'
						}
					},
					{
						text: '删除',
						style: {
							backgroundColor: '#dd524d'
						}
					}
				],
				doc_list: [],
				departmentName_list: []

			}
		},

		onLoad() {

			uni.setStorageSync('current', 0);

			if (uni.getStorageSync('global_status') == "0") {
				this.options = [{
					text: '下载',
					style: {
						backgroundColor: '#9EB7EC'
					}
				}];
				this.add_able = false;
			}
		},
		//获得数据
		onShow() {
			this.current = uni.getStorageSync('current');
			console.log(this.current);

			uni.request({
				url: helper.websiteUrl + '/announcement/getAll',
				data: {},
				method: 'GET',
				header: {
					"token": uni.getStorageSync('token')
				},
				success: (res) => {
					if (res.data.code == 200) {
						uni.setStorageSync('global_announcement_list', res.data.data);
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
						uni.setStorageSync('global_read_list', res.data.data);


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
					console.log('未读列表');
					console.log(res.data);
					if (res.data.code == 200) {
						uni.setStorageSync('global_unread_list', res.data.data);

					}
				}
			});

			//公告页面
			console.log("身份为：" + uni.getStorageSync('global_status'));
			//对身份取反
			if (uni.getStorageSync('global_status') == '1') {
				this.viewAble = true;
				this.viewUnable = false;
			} else if (uni.getStorageSync('global_status') == '0') {
				this.viewAble = false;
				this.viewUnable = true;
			}
			console.log("this.viewAble" + this.viewAble);
			//决定能否滑动操作
			if (uni.getStorageSync('global_status') == '1') {
				this.isDelete = false;
			} else if (uni.getStorageSync('global_status') == '0') {
				this.isDelete = true; //不能滑动
			}

			this.value1 = 1;
			//this.current = 0;
			//获得公告列表
			this.list = uni.getStorageSync('global_announcement_list');


			//下载中心页面

			uni.request({
				url: helper.websiteUrl + '/document/getAll',
				method: 'GET',
				header: {
					"token": uni.getStorageSync('token')
				},
				success: (res) => {
					if (res.data.code == 200) {
						this.doc_list = res.data.data.reverse();

					} else {
						this.showToast(res.data.message, 'error');
					}
				}
			});

			uni.request({
				url: helper.websiteUrl + '/department/getAll',
				method: 'GET',
				header: {
					"token": uni.getStorageSync('token')
				},
				success: (res) => {
					if (res.data.code == 200) {
						this.department_list = res.data.data;
						this.departmentName_list = []; //清空
						for (let i = 0; i < this.department_list.length; i++) {
							this.departmentName_list.push(this.department_list[i].departmentName);
						}
					} else {
						this.showToast(res.data.msg);
					}
				}
			});


		},


		methods: {
			confirmdelete() {

				uni.request({ //http://p40974t583.qicp.vip/announcement/delete
					url: helper.websiteUrl + '/announcement/delete', //链接地址
					data: {
						//此处为整个信息
						"title": this.list[this.delete_index].title,
						"content": this.list[this.delete_index].content,
						"createDate": this.list[this.delete_index].createDate,
						"initiatorName": this.list[this.delete_index].initiatorName
					},
					dataType: 'json',
					method: 'POST',
					header: {
						"token": uni.getStorageSync('token')
					},
					success: res => {
						console.log(res.data);
						if (res.data.code == 200) { //删除部门成功
							/* 	this.$refs.uToast.show({
																	title: res.data.message,
																	type: 'success'
																}) */
							this.list.splice(this.delete_index, 1);
							uni.request({
								url: helper.websiteUrl + '/announcement/getAll',
								data: {},
								method: 'GET',
								header: {
									"token": uni.getStorageSync('token')
								},
								success: (res) => {
									if (res.data.code == 200) {
										uni.setStorageSync('global_announcement_list', res.data
											.data);
									} else {
										this.$refs.uToast.show({
											title: '获取公告信息失败',
											type: 'error'
										})
									}
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
			},
			change(index) {
				this.current = index;
				uni.setStorageSync('current', index);
				//console.log("this.current" + this.current);

			},


			async gethad() {
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

							//this.dataSet(res.data.data);
							console.log(res.data.data);
							temp = res.data.data;
							console.log(temp);
						}
					}
				});
			},
			//公告页面

			changeDrop() {
				console.log("value1改变为:" + this.value1);
				//全部
				if (this.value1 == 1) {
					this.list = uni.getStorageSync('global_announcement_list');

				}
				//已读
				else if (this.value1 == 2) {
					console.log(" this.id :" + this.id);
					this.list = uni.getStorageSync('global_read_list');


				}
				//未读
				else if (this.value1 == 3) {
					console.log(uni.getStorageSync('global_unread_list'));
					this.list = uni.getStorageSync('global_unread_list');

				}
			},
			//添加按钮事件
			fabClick2() {
				uni.navigateTo({
					url: '../announcementAdd/announcementAdd'
				});
			},


			click2(index1, index2) {
				console.log(this.list[index1].title);
				console.log("打印");
				this.delete_index = index1;
				this.showdelete = true;
				console.log(this.delete_index);

				/* 				//重新获取
								uni.request({ //http://p40974t583.qicp.vip/announcement/getAll
									url: helper.websiteUrl + '/announcement/getAll', //链接地址
									data: {},
									dataType: 'json',
									method: 'GET',
									header: {
										"token": uni.getStorageSync('token')
									},
									success: res => {
										console.log(res.data);
										if (res.data.code == 200) {
											console.log("刷新成功");
											//this.dataSet(res.data.data);
											//console.log(res.data.Data.length);
											this.list = res.data.data;
										}
									}
								}); */

			},

			//点击卡片后跳转到详情页面
			clickbranch(indexCard) {
				console.log(indexCard);
				//存储打开的公告标题到本地
				uni.setStorage({
					key: 'announcementTitle',
					data: this.list[indexCard].title,

					success: (res) => {
						console.log("存入公告title成功");
						this.branch();
					}

				});




			},
			branch() {
				//跳转页面
				uni.navigateTo({
					url: '../announcementDetail/announcementDetail'
				})

			},


			openDrop(index) {
				// 展开某个下来菜单时，先关闭原来的其他菜单的高亮
				// 同时内部会自动给当前展开项进行高亮
				this.$refs.uDropdown.highlight();
			},
			closeDrop(index) {
				// 关闭的时候，给当前项加上高亮
				// 当然，您也可以通过监听dropdown-item的@change事件进行处理
				this.$refs.uDropdown.highlight(index);
			},
			//下载中心页面
			//tab切换


			confirm() {
				this.show_progress = false;
			},
			showTips(Msg) {
				this.$refs.uTips.show({
					title: Msg
				});
			},

			image_select(str) {

				let i = str.lastIndexOf(".");

				var s = "../../static/";
				var ss = ".png";
				if (str.slice(i + 1) == 'docx' || str.slice(i + 1) == 'pdf' || str.slice(i + 1) == 'ppt' || str.slice(i +
						1) == 'zip' || str.slice(i + 1) == 'jpg' || str.slice(i + 1) == 'png' || str.slice(i + 1) ==
					'xlsx' || str.slice(i + 1) == 'doc' || str.slice(i + 1) == 'jpeg') {
					return s + str.slice(i + 1) + ss;
				} else {
					return s + "unknow" + ss;
				}
			},
			refresh() {
				uni.request({
					url: helper.websiteUrl + '/document/getAll',
					method: 'GET',
					header: {
						"token": uni.getStorageSync('token')
					},
					success: (res) => {
						if (res.data.code == 200) {
							this.doc_list = res.data.data.reverse();

						} else {
							this.showToast(res.data.message, 'error');
						}
					}
				});
			},
			click(index, index1) {
				//删除文件
				if (index1 == 1) {
					uni.request({
						url: helper.websiteUrl + '/document/delete',
						data: {
							"title": this.doc_list[index].title
						},
						header: {
							"token": uni.getStorageSync('token')
						},
						method: 'POST',
						success: (res) => {
							console.log(res.data);
							if (res.data.code == 200) {
								this.showToast(res.data.message, 'success');
								this.refresh();
							} else {
								this.showToast(res.data.res.message, 'error');
							}
						}
					})
				}
				//下载文件
				else {
					uni.request({
						url: helper.websiteUrl + '/document/download',
						data: {
							"title": this.doc_list[index].title,
							"initiatorName": this.doc_list[index].initiatorName,
							"createDate": this.doc_list[index].createDate,
							"url": this.doc_list[index].url,
							"departmentName": this.doc_list[index].departmentName
						},
						header: {
							"token": uni.getStorageSync('token')
						},
						method: 'POST',
						success: (res) => {
							if (res.data.code == 200) {
								console.log(res.data);
								console.log('downloadFile');
								this.show_progress = true;

								//this.playpapers(res.data.data);
								const downloadTask = uni.downloadFile({
									url: res.data.data,
									header: {
										"token": uni.getStorageSync('token')
									},
									success: (res1) => {
										if (res1.statusCode == 200) {
											this.show1 = true;
											console.log("临时路径" + res1.tempFilePath);
											let that = this;
											uni.saveFile({
												tempFilePath: res1.tempFilePath,
												success: function(red) {
													that.luj = red.savedFilePath;

													uni.openDocument({
														filePath: red
															.savedFilePath,
														success: (res) => {
															console.log(
																'成功打开文档'
															);

														}

													})
												}
											});
										} else {
											this.showToast('下载失败', 'error');
										}
									}
								});

								downloadTask.onProgressUpdate((res1) => {
									this.percent = res1.progress;
								});
							} else {
								this.showToast(res.data.res.message, 'error');
							}
						}
					})
				}
			},
			showToast(Msg, Type) {
				this.$refs.uToast.show({
					title: Msg,
					type: Type
				})
			},
			fabClick() {
				uni.setStorageSync('current', 1);
				console.log('上传文件');
				uni.navigateTo({
					url: '../downloadCenter/upload?token=' + encodeURIComponent(JSON.stringify(uni.getStorageSync(
							'token'))) +
						"&departmentName=" + encodeURIComponent(JSON.stringify(this.departmentName_list))
				});
			},
			search() {
				console.log('search');
				console.log('要搜索的关键字' + this.keyword);
				uni.request({
					url: helper.websiteUrl + '/document/searchByTitle',
					data: {
						"title": this.keyword
					},
					method: 'POST',
					header: {
						"token": uni.getStorageSync('token')
					},
					success: (res) => {
						console.log(res.data);
						if (res.data.code == 200) {
							this.doc_list = res.data.data;
						} else {
							this.showToast(res.data.message, 'error');
						}
					}
				})

			}

		}
	}
</script>

<style scoped lang="scss">
	page {
		background-color: #D8E8E0;
	}

	.card {
		background-color: #D8E8E0;
	}

	.top {}

	.dropdown {
		background-color: #98C080;
	}

	.btnfab {
		size: 20rpx;
		margin-top: 0rpx;
	}

	.tab {

		bar-width: 70%;
		active-color: #9EC2EC;
	}

	.u-line {}

	.uni_btnImage {}

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

	.cu-card.dynamic>.cu-item>.text-content {
		margin-bottom: 1px;
		margin-top: 6px;
	}

	.card-box {
		background-image: url(../../static/CardImage.png);
		border-radius: 35rpx;
		/*f4f4f5*/
		box-shadow: 12 12 12 12 rgba(0, 0, 0, 0);
		/* 加阴影*/
		-moz-box-shadow: 2px 2px 10px #8a908f;
		-webkit-box-shadow: 2px 2px 10px #8a908f;
		box-shadow: 2px 2px 10px #8a908f;
	}
</style>
