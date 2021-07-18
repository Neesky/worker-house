<template>
	<view class="content">
		<view>
			<u-toast ref="uToast" />
		</view>
	
		<view class="card1">
			<view class="position" style="font-weight: 700;font-size: 40rpx;">
				{{departmentName}}
			</view>
			<u-line color="#d6f4f7"></u-line>
			<textarea :disabled=true v-model="detail" :auto-height=true style="background-color: #FFFFFF; padding:20px;height:800rpx;color:#999999;width: 600rpx;"></textarea>
		</view>
		
		<view class="u-form" v-for="(item,index) in list" :key="index">
			<view class="card">
				<view class="position" style="font-weight: 700;font-size: 40rpx;">
					{{item.position}}
				</view>
				<u-line color="#d6f4f7"></u-line>

				<uni-grid :column="3" :showBorder="false" :square="false">
					<view class="members" v-for="(name,index) in item.members" :key="index">
						<uni-grid-item>
							<view class="nameview">
								<u-icon name="arrow-right" size="24rpx"></u-icon>
								<text style="font-size: 35rpx;">{{name}}</text>
							</view>
						</uni-grid-item>
					</view>
				</uni-grid>
			</view>
		</view>
	</view>
</template>

<script>
	import helper from '../../common/base.js'
	export default {
		data() {
			return {
				list: [],
				departmentName: '',
				detail:''
			}
		},

		//获得上个页面的部门名称
		onLoad() { //option为object类型，会序列化上个页面传递的参数
			uni.getStorage({
				key: 'clickBranch',
				success: (res) => {
					this.departmentName = res.data.departmentName;
					this.detail = res.data.departmentRemark;
					console.log('获取部门详细信息');
					console.log(this.departmentName);

					uni.request({
						url: helper.websiteUrl + '/employee/search',
						method: 'POST',
						data: {
							"departmentName": this.departmentName
						},
						header: {
							"token": uni.getStorageSync('token')
						},
						success: (res) => {
							if (res.data.code == 200) {
								console.log("连接成功");
								this.solve(res.data.data);
							} else {
								console.log("此部门暂无员工");
								this.$refs.uToast.show({
									title: '此部门暂无员工',
									type: 'warning'
								})
							}
						}
					});
				}
			})
		},
		methods: {
			isIn(name, ss) {
				for (let i = 0; i < ss.length; i++) {
					if (ss[i] == name) {
						return true;
					}
				}
				return false;
			},
			solve(mem) {

				let jobNameList = [];

				if (mem != null) {
					//console.log("mem.length:"+mem.length)
					for (let i = 0; i < mem.length; i++) {
						if (this.isIn(mem[i].jobName, jobNameList) == false) {
							jobNameList.push(mem[i].jobName);
						}
					}
					//console.log(jobNameList);
					for (let i = 0; i < jobNameList.length; i++) {
						let temp = {
							"position": '',
							"members": []
						};
						temp.position = jobNameList[i];
						for (let j = 0; j < mem.length; j++) {
							if (mem[j].jobName == jobNameList[i]) {
								temp.members.push(mem[j].name);
								//	console.log(temp);
								//console.log(jobNameList[i] + "加入" + mem[j].name);
							}
						}
						//		console.log(temp);

						this.list.push(temp);

					}

				}
			}

		}
	}
</script>

<style>
	page {
		background-color: #E9E4FE;
	}

	/*.content{
		margin-top: 0rpx;
		background-color: ##f8f7f8;
	}*/

	.card {
		margin-top: 40rpx;
		margin-left: 25rpx;
		width: 93%;
		background-color: #fdfdfd;
		flex: 1;
		justify-content: center;
		align-items: center;
		border-width: 1;
		height: 300rpx;
		border-radius: 10rpx;
	}
	
	.card1{
		margin-top: 40rpx;
		margin-left: 25rpx;
		width: 93%;
		background-color: #fdfdfd;
		flex: 1;
		justify-content: center;
		align-items: center;
		border-width: 1;
		border-radius: 10rpx;
	}
	
	.position {
		display: flex;
		justify-content: center;
		align-items: center;
		height: 80rpx;


	}

	.members {
		margin-top: 3rpx;
		margin-left: 0rpx;
	}

	.nameview {
		margin-left: 12rpx;
	}
</style>
